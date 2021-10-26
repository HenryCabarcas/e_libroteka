<template>
  <div class="book-container">
    <div v-if="success === -1" class="loading-bar">
      <va-progress-bar indeterminate size="large" />
    </div>

    <div v-if="success === 1">
      <div class="book-info">
        <div class="book-img">
          <img :src="book.url" />
        </div>
        <div class="book-text">
          <h1>{{ book.title }}</h1>
          <va-card color="primary" gradient class="book-genders">
            <va-card-title>Title</va-card-title>
            <va-card-content
              >Lorem ipsum dolor sit amet, consectetur adipiscing
              elit.</va-card-content
            >
          </va-card>
        </div>
      </div>
      <Comments :isbn="isbn" />
    </div>
    <div v-if="success === 0">No funciona</div>
  </div>
</template>

<script>
import axios from "axios";
import Comments from "@/components/Comments.vue"

export default {
  name: "Book",
  components: {
    Comments
  },
  data() {
    return {
      book: {},
      isbn: "",
      success: -1,
    };
  },
  beforeMount() {
    this.isbn = this.$route.params.isbn;
    console.log(this.isbn)
    axios
      .get(process.env.VUE_APP_BACK_END_URL + "book/?isbn=" + this.isbn)
      .then((response) => {
        this.book = response.data.result[0];
        console.log(this.book)
        this.success = 1;
      })
      .catch((error) => {
        this.success = 0;
      });
  },
};
</script>

<style lang="scss" scoped>
.book-container {
  display: block;
  margin: 2rem 5rem;
  padding: 1rem 1rem;
  background-color: rgba(255, 255, 255, 0.739);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 12px;
  text-align: left;
}
h1 {
  font-size: 24pt;
}
.book-info {
  display: flex;
  justify-content: space-between;
  margin: 1rem 1rem;
}
.book-img {
  padding: 0;
  margin: 0;
  display: block;
  width: 128px;
  border-radius: 8px;
}
.book-text {
  display: flex;
  flex-direction: column;
  margin-left: 1rem;
  margin-right: auto;
  width: 100%;
}
.book-genders {
  display: block;
  width: 50%;
  color: black;
}
</style>
