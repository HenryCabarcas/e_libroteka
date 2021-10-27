<template>
  <div id="search-results">
    <div class="results-titles">
      <span class="item-title"></span>
      <span class="item-title">Title</span>
      <span class="item-authors">Author/s</span>
      <span class="item-genders">Gender/s</span>
      <span class="item-pages">Pages</span>
    </div>
    <div v-for="item in results" :key="item.id">
      <SearchServiceOne
        :all="item"
        :title="item.volumeInfo.title"
        :authors="item.volumeInfo.authors ? item.volumeInfo.authors : []"
        :image="
          item.volumeInfo.imageLinks
            ? item.volumeInfo.imageLinks.smallThumbnail
            : '../assets/book_default.png'
        "
        :genders="item.volumeInfo.categories ? item.volumeInfo.categories : []"
        :pages="item.volumeInfo.pageCount ? item.volumeInfo.pageCount : 0"
      ></SearchServiceOne>
    </div>
  </div>
</template>

<script>
import SearchServiceOne from "./SearchServiceOne.vue";
export default {
  name: "SearchServiceResults",
  components: {
    SearchServiceOne,
  },
  props: {
    results: Array,
  },
};
</script>

<style>
#search-results {
  width: 70%;
  overflow: hidden;
  border-radius: 24px;
  background: rgba(214, 224, 255, 0.8);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2.5px);
  -webkit-backdrop-filter: blur(2.5px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  animation: resultsUp 250ms ease-in-out;
}
@keyframes resultsUp {
  0% {
    transform: translateY(80vh);
  }
  100% {
    transform: translateY(0);
  }
}
.results-titles {
  display: grid;
  width: 100%;
  text-align: left;
  vertical-align: center;
  align-items: center;
  padding: 4px;
  grid-column-gap: 10px;
  grid-template-columns: 80px 35% 20% 20% 10%;
  font-weight: 700;
}
.item-title {
  display: inline-block;
  grid-column-start: 2;
  grid-column-end: 3;
  width: fit-content;
  font-weight: 600;
}
.item-authors {
  display: inline-block;
  grid-column-start: 3;
  grid-column-end: 4;
}
.item-genders {
  display: inline-block;
  grid-column-start: 4;
  grid-column-end: 5;
}
.item-pages {
  display: inline-block;
  grid-column-start: 5;
  grid-column-end: 6;
}
</style>
