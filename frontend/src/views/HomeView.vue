<template>
  <div>
    <Navbar/>
    <v-container fluid>
      place some analytics here
    </v-container>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";

export default {
  name: "Home",

  components: {
    Navbar,
  },
};
</script>
