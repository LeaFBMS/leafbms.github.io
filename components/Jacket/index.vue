<template>
  <div>
    <h1>Data from JSON</h1>
    <pre>{{ jsonData }}</pre>
  </div>
</template>

<script>
export default {
  async asyncData({$axios}) {
    try {
      console.log("run");
      const jsonData = await $axios.$get("@data/tracks.json"); // Specify your JSON file path here
      return {jsonData};
    } catch (error) {
      console.error("Error loading JSON:", error);
    }
  },
};
</script>
