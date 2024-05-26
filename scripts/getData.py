# %%
import re
import time
import pandas as pd
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

# %%
driver = webdriver.Edge()
driver.get("https://soundcloud.com/leaf-7/tracks")

# %%
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.TAG_NAME, "li.soundList__item")))
time.sleep(5)

# %%
# Scroll to the end of the page
scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(scroll_pause_time)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all tracks
track_elements = driver.find_elements(By.CSS_SELECTOR, "li.soundList__item")

# %%
producers = []
track_names = []
times = []
track_urls = []
jacket_urls = []

url_pattern = re.compile(r'url\("([^"]+)"\)')

for track_element in track_elements:
    title_element = track_element.find_element(
        By.CSS_SELECTOR, ".soundTitle__titleContainer"
    )
    track_title = title_element.text.split("\n")

    producer = track_title[1]
    track_name = track_title[2]
    t = track_title[4]  # time

    # Extract song URL
    track_url_element = track_element.find_element(
        By.CSS_SELECTOR, ".sound__artwork > a"
    )
    track_url = track_url_element.get_attribute("href")

    try:
        sound_artwork_div = track_element.find_element(By.CLASS_NAME, "sound__artwork")
        sound_artwork_span = sound_artwork_div.find_element(By.TAG_NAME, "span")
        sound_artwork_style = sound_artwork_span.get_attribute("style")
        track_jacket_url = re.search(url_pattern, sound_artwork_style).group(1)
    except AttributeError:
        continue

    producers.append(producer)
    track_names.append(track_name)
    times.append(t)
    track_urls.append(track_url)
    jacket_urls.append(track_jacket_url)


# %%
tracks_df = pd.DataFrame(
    {
        "Producer": producers,
        "Track Name": track_names,
        "Time": times,
        "URL": track_urls,
        "Jacket URL": jacket_urls,
    }
)

# %%
# Should be MARENOL
print(tracks_df.iloc[11, -1])

# %%
driver.close()

# %%
here = Path(__file__).parent.parent
print(here)

# %%
save_path = here / "data" / "tracks.csv"
tracks_df.to_csv(save_path, index=False)

# %%
