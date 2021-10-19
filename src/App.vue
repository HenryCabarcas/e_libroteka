<template>
  <nav id="navbar" class="blur">
    <div id="navbar-left">
      <router-link to="/">
        <va-button flat> Home </va-button>
      </router-link>
      <router-link to="/about">
        <va-button flat> About </va-button>
      </router-link>
    </div>
    <div id="navbar-center" v-if="this.$route.path !== '/'">
      <SearchBar />
    </div>
    <div id="navbar-right">
      <va-button color="success" gradient class="mr-4">
        <router-link to="/register-book">Register</router-link>
      </va-button>
    </div>
  </nav>
  <router-view />
  <h2>Hola mundo</h2>
</template>
<script>
import SearchBar from "@/components/SearchBar.vue";
export default {
  name: "App",
  components: { SearchBar },
};
</script>
<style lang="scss">
:root {
  font-family: Avenir, sans-serif;
}
#app {
  font-family: Avenir, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-top: 50px;
  background-image: url("./assets/back_clear.svg");
  background-size: 400px;
  background-repeat: repeat;
  background-attachment: fixed;
}
#navbar {
  position: fixed;
  z-index: 2;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  padding: 1rem 0;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 50px;
  background: rgba(255, 255, 255, 0.562);

  border-bottom: 1px solid rgba(255, 255, 255, 0.18);
}
#navbar > div {
  margin-left: 12px;
  margin-right: 12px;
  padding: 0.75rem;
}
#navbar-left {
  display: block;
}
#navbar-center {
  display: block;
  flex: 1;
}
#navbar-right {
  display: block;
}
</style>
