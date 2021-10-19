<template>
  <div class="result-container">
    <span class="result-title">
      {{ title }}
    </span>
    <span v-if="author.length > 1">-</span>
    <span class="result-author">
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
  display: flex;
  align-content: center;
  align-items: center;
  justify-content: stretch;
  width: 100%;
  cursor: pointer;
  padding: 0.5rem 1rem;
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
}
.result-author {
  color: gray;
}
</style>
