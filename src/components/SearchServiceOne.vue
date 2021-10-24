<template>
  <div class="item-container" @click="goto()">
    <img :src="image" />
    <span class="item-title">{{ title }}</span>
    <span class="item-authors">{{ authors.join(", ") }}</span>
    <span class="item-genders">{{ genders.join(", ") }}</span>
    <span class="item-pages">{{ pages }}</span>
  </div>
</template>

<script>
export default {
  name: "SearchServiceOne",
  props: {
    title: String,
    authors: Array,
    image: String,
    genders: Array,
    pages: Number,
    all: Object
  },
  methods: {
    goto() {
    }
  }
}
</script>

<style lang="scss">
.item-container {
  display: grid;
  width: 100%;
  height: 120px;
  grid-column-gap: 10px;
  padding: 4px;
  text-align: left;
  vertical-align: center;
  align-items: center;
  grid-template-columns: 80px 35% 20% 20% 10%;
  margin-bottom: 2px;
  cursor: pointer;
  img {
    margin-left: 4px;
    max-height: 112px;
    max-width: 80px;
    width: fit-content;
    grid-column-start: 1;
    grid-column-end: 2;
  }
}
.item-container:hover {
  background-color: rgba(0, 0, 0, 0.25);
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