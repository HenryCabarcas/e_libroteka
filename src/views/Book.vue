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
          <div class="book-genders">
            <va-chip v-for="item in genders" :key="item" flat>
              {{ item }}
            </va-chip>
          </div>
          <div class="score">
            <va-rating v-model="score" color="warning" readonly size="medium" />
            <p>Based on {{ reviews }} opinions.</p>
          </div>
        </div>
      </div>
      <Comments :isbn="isbn" />
    </div>
    <div v-if="success === 0">No funciona</div>
  </div>
</template>

<script>
import axios from "axios";
import Comments from "@/components/Comments.vue";

export default {
  name: "Book",
  components: {
    Comments,
  },
  data() {
    return {
      book: {},
      isbn: "",
      success: -1,
      genders: [],
      score: 0,
      reviews: 0,
    };
  },
  beforeMount() {
    this.isbn = this.$route.params.isbn;
    console.log(this.isbn);
    axios
      .get(process.env.VUE_APP_BACK_END_URL + "book/?isbn=" + this.isbn)
      .then((response) => {
        this.book = response.data.result[0];
        this.genders = String(this.book.gender).split(",");
        console.log(this.book);
        this.book.comments.forEach((item) => {
          this.reviews += 1;
          this.score += item.score;
        });
        if (this.reviews > 0) this.score /= this.reviews;
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
