<template>
  <nav id="navbar" class="blur">
    <div id="navbar-left">
      <router-link to="/">
        <img id="e-libroteka" src="@/assets/ELibroteka.png" alt="e-libroteka" />
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
import axios from "axios";
export default {
  name: "App",
  components: { SearchBar },
  data() {
    return {
      bg_url: ""
    }
  },
  beforeCreate() {
    let apiKey = "VKS5Pto4LE5EmgloPZKASfuGUpMbPYrR4lwCwJGERTw"
    axios
      .get("https://api.unsplash.com/photos/random?query=read&orientation=landscape&client_id=" + apiKey)
      .then(response => {
        this.bg_url = response.data.urls.regular;
        document.getElementById("app").style.backgroundImage = `url('${this.bg_url}')`;
      })
  }
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
  background-size: 100%;
  min-height: 100vh;
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
  user-select: none;
  border-bottom: 1px solid rgba(255, 255, 255, 0.18);
}
#navbar > div {
  margin-left: 12px;
  margin-right: 12px;
  padding: 0.75rem;
}
#navbar-left {
  display: flex;
  flex-direction: row;
  div,
  img {
    display: block;
    margin-right: 4px;
    color: black;
    cursor: pointer;
  }
}
#navbar-center {
  display: flex;
  width: 70%;
}
#navbar-right {
  display: block;
}
#e-libroteka {
  display: inline-block;
  height: 100%;
}
</style>
