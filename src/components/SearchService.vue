<template>
  <div id="search-container">
    <div id="search-bar">
      <div id="search-bar-grid">
        <span id="search-input">
          <va-input
            v-model="query"
            @keydown.enter="search()"
            placeholder="Search"
            @focus="onFocus()"
            @blur="onBlur()"
            outline
          />
        </span>
        <span id="search-button">
          <va-button
            color="info"
            flat
            @click="search()"
            icon-right="search"
          ></va-button>
        </span>
      </div>
    </div>
    <div id="separator"></div>
    <SearchServiceResults
      :results="results"
      v-if="results.length > 0"
    ></SearchServiceResults>
  </div>
</template>

<script>
import axios from "axios";
import SearchServiceResults from "./SearchServiceResults.vue";
export default {
  name: "SearchService",
  data() {
    return {
      query: "",
      results: [],
      waitingResults: false
    }
  },
  components: {
    SearchServiceResults
  },
  methods: {
    search() {
      if (this.query.length > 1 && !this.waitingResults) {
        this.waitingResults = true;
        this.results = []
        axios
          .get("https://www.googleapis.com/books/v1/volumes?maxResults=40&q=" + this.query)
          .then((response) => {
            this.waitingResults = false;
            this.results = response.data.items;
            console.log(this.results);

          }).catch(error => {
            this.waitingResults = false;

          })
      }
    },
    onFocus() {
      let sb = document.getElementById("search-bar-grid")
      sb.style.backgroundColor = "rgba(20,20,20,0.35)"
      sb.style.border = "1px solid white"
    },
    onBlur() {
      let sb = document.getElementById("search-bar-grid")
      sb.style.backgroundColor = "rgba(20,20,20,0.15)"
      sb.style.border = "1px solid transparent"


    }
  },
}
</script>

<style lang="scss">
#search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-content: center;
  justify-content: center;
}
#search-bar {
  display: block;
  padding: 4px;
  width: 50%;
}
#search-bar-grid {
  display: grid;
  align-self: center;
  grid-template-columns: 85% 15%;
  height: fit-content;
  align-items: center;
  align-content: center;
  justify-content: center;
  padding: 4px;
  background-color: rgba(1, 1, 1, 0.25);
  border-radius: 100px;
  border: 1px solid transparent;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  * {
    color: white;
    font-weight: 600;
  }
  width: 100%;
}

#search-input {
  display: block;
  align-items: center;
  align-content: center;
  justify-content: center;
  grid-column-start: 1;
  grid-column-end: 2;
  * {
    border: none;
    background-color: transparent;
  }
}
#search-button {
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
  grid-column-start: 2;
  grid-column-end: 3;
  * {
    width: 100%;
  }
}
#separator {
  height: 75px;
}
</style>