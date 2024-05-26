<template>
  <div>
    <ul>
      <li v-for="item in jsonData" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      jsonData: [],
    };
  },
  async asyncData() {
    // Fetch data from the JSON file
    const jsonData = await require("@data/tracks.json");

    // Return the data to be used in the component
    return {jsonData};
  },
};
</script>
