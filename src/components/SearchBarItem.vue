<template>
  <div class="result-container">
    <span class="result-title">
      {{ title }}
    </span>
    <span class="result-author" v-if="author.length > 1">
      {{ author }}
    </span>
  </div>
</template>

<script>
export default {
  name: "SearchBarItem",
  props: {
    title: String,
    author: String,
  },
};
</script>

<style>
.result-container {
  position: relative;
  display: grid;
  grid-column-gap: 10px;
  text-align: left;
  vertical-align: center;
  align-items: center;
  grid-template-columns: 50% 50%;
  width: 100%;
  height: 48px;
  cursor: pointer;
}
.result-container:hover {
  background-color: rgba(0, 0, 0, 0.15);
}
.result-container > span {
  display: block;
  text-align: left;
  align-items: flex-start;
  max-width: 50%;
}
.result-title {
  font-weight: 600;
  grid-column-start: 1;
  grid-column-end: 2;
  padding: 0 1rem;
  margin: 2px 8px;
}
.result-author {
  color: gray;
  grid-column-start: 2;
  grid-column-end: 3;
}
</style>
