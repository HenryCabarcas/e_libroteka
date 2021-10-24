<template>
  <div class="home">
    <img src="@/assets/banner.png" id="banner" />
    <SearchService></SearchService>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchService from "@/components/SearchService.vue";

export default {
  name: "Home",
  components: {
    SearchService,
  },
  created() {
    console.log(this.$route);
  },
};
</script>

<style lang="scss">
#banner {
  padding-bottom: 5%;
  padding-top: 5%;
}
</style>
