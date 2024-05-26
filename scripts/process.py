# %%
import os
import csv
import json
import requests

from pathlib import Path
from PIL import Image

root = Path(__file__).parent.parent
data_folder = root / "data"
jackets_folder = data_folder / "jackets"

# %%
tracks = []
with open(data_folder / "tracks.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tracks.append(row)

# %%
print(tracks)

with open(data_folder / "tracks.json", "w") as file:
    json.dump(tracks, file, indent=4)
# %%
if not os.path.exists(jackets_folder):
    os.makedirs(jackets_folder)

# %%
for track in tracks:
    jacket_url = track["Jacket URL"]
    track_name = track["Track Name"]
    track_name = track_name.replace("/", "-")

    jacket_path = jackets_folder / f"{track_name}.jpg"
    webp_path = jackets_folder / f"{track_name}.webp"

    response = requests.get(jacket_url)
    if response.status_code == 200:
        with open(jacket_path, "wb") as f:
            f.write(response.content)

    # JPG to WebP
    if os.path.exists(jacket_path):
        image = Image.open(jacket_path)
        image.save(webp_path, "WEBP")

        os.remove(jacket_path)

# %%
