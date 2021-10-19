<template>
  <div id="search-bar">
    <va-input
      v-model="query"
      placeholder="Search"
      @click="clicked(true)"
      @blur="clicked(false)"
    />
  </div>
  <div id="results" v-if="showList">
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
          .get("https://www.googleapis.com/books/v1/volumes?q=" + this.query)
          .then((response) => {
            this.results = response.data.items;
            console.log(this.results);
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

<style>
#results {
  position: absolute;
  display: block;
  align-self: center;
  align-items: center;
  top: 100%;
  left: 0;
  width: 100%;
  padding: 1rem;
  background-color: aqua;
  z-index: 12;
}
</style>
