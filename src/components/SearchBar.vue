<template>
  <div id="nav-search-bar">
    <va-input
      v-model="query"
      placeholder="Search"
      @click="clicked(true)"
      @blur="clicked(false)"
    />
  </div>
  <div id="nav-results" v-if="showList">
    <div v-for="item in this.results" :key="item.id">
      <SearchBarItem
        :title="item.volumeInfo.title"
        :author="item.volumeInfo.authors ? item.volumeInfo.authors[0] : ' '"
      />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import _ from "lodash";
import SearchBarItem from "./SearchBarItem.vue";
export default {
  name: "SearchBar",
  components: {
    SearchBarItem,
  },
  data() {
    return {
      query: "",
      results: [],
      showList: false,
    };
  },
  created() {
    this.debouncedGetAnswer = _.debounce(this.search, 500);
  },
  methods: {
    clicked(value) {
      this.showList = value;
    },
    search() {
      if (this.query.length > 1) {
        axios
          .get(process.env.VUE_APP_GOOGLE_BOOK_URL + "?q=" + this.query)
          .then((response) => {
            this.results = response.data.items;
          });
        this.clicked(true);
      }
    },
  },
  watch: {
    query: function (newQuery, oldQuery) {
      this.debouncedGetAnswer();
    },
  },
};
</script>

<style lang="scss">
#nav-search-bar {
  display: block;
  width: 100%;
  align-items: center;
  align-content: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.479);
  border-radius: 100px;
  border: 1px solid transparent;
  backdrop-filter: blur(5px);
  margin: 5px 4%;
  -webkit-backdrop-filter: blur(5px);
  * {
    border: none;
    background-color: transparent;
    height: 100%;
  }
}
#nav-results {
  position: absolute;
  display: block;
  align-self: center;
  align-items: center;
  top: 100%;
  left: 0;
  right: 0;
  overflow: hidden;
  margin: 6px 15%;
  border-radius: 12px;
  background-color: rgba(255, 255, 255, 0.842);
  backdrop-filter: blur(2.5px);
  -webkit-backdrop-filter: blur(2.5px);
  box-shadow: 20px 20px 60px #0000009b, -20px -20px 60px#0303032F;
  z-index: 12;
}
</style>
