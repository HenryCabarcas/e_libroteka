<template>
  <div class="book-container">
    <div v-if="success === -1" class="loading-bar">
      <va-progress-bar indeterminate size="large" />
    </div>
    <div v-if="success === 1">
      <div class="book-header">
        <div class="book-info">
          <div class="book-img">
            <img :src="book.url" />
          </div>
          <div class="book-text">
            <h1>{{ book.title }}</h1>
            <h5 v-for="item in authors" :key="item" class="author">
              {{ item }}
            </h5>
            <div class="book-genders">
              <va-chip v-for="item in genders" :key="item" flat>
                {{ item }}
              </va-chip>
            </div>
          </div>
        </div>
      </div>
      <va-divider />

      <div class="book-footer">
        <div class="foot-left">
          <div class="book-chip" v-if="book.isbn !== undefined">
            <p class="book-chip-text">Document ISBN:</p>
            <va-chip size="small" flat>
              {{ book.ISBN }}
            </va-chip>
          </div>
          <div class="book-chip" v-if="book.publicationDate !== undefined">
            <p class="book-chip-text">Publication Year:</p>
            <va-chip size="small" flat>
              {{ book.publicationDate }}
            </va-chip>
          </div>
          <div class="book-chip" v-if="book.format !== undefined">
            <p class="book-chip-text">Document format:</p>
            <va-chip size="small" flat>
              {{ book.format }}
            </va-chip>
          </div>
          <div class="book-chip" v-if="book.pages > 0">
            <p class="book-chip-text">Pages number:</p>
            <va-chip size="small" flat>
              {{ book.pages }}
            </va-chip>
          </div>
        </div>
        <div class="foot-right">
          <div class="score">
            <va-rating v-model="score" color="warning" readonly />
            <p>Based on {{ reviews }} opinions.</p>
          </div>
        </div>
      </div>
      <div class="book-resume">
        <h3>Resume</h3>
        <va-divider />
        <p>
          {{ book.resume }}
        </p>
      </div>
      <Comments :isbn="isbn" />
    </div>
    <div v-if="success === 0">
      <h1><b>404</b>: Not Found</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Comments from "@/components/Comments.vue";
import { useRouter } from "vue-router";
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
      authors: [],
      score: 0,
      reviews: 0,
      loading: false,
      upt: true,
    };
  },
  methods: {
    forceUpdateInfo() {
      this.upt = false;
      this.updateInfo();
    },
    updateInfo() {
      if (!this.loading && !this.upt) {
        this.loading = true;
        this.isbn = this.$route.params.isbn;
        console.log(this.isbn);
        axios
          .get(process.env.VUE_APP_BACK_END_URL + "book/?isbn=" + this.isbn)
          .then((response) => {
            this.book = response.data.result[0];
            this.genders = String(this.book.gender).split(",");
            this.authors = String(this.book.author).split(",");
            console.log(this.book);
            this.book.comments.forEach((item) => {
              this.reviews += 1;
              this.score += item.score;
            });
            if (this.reviews > 0) this.score /= this.reviews;
            this.success = 1;
            this.upt = true;
            this.loading = false;
          })
          .catch((error) => {
            this.loading = false;
            this.upt = true;
            this.success = 0;
          });
      }
    },
  },

  updated() {
    this.updateInfo();
  },
  beforeMount() {
    this.upt = false;
    this.updateInfo();
  },
  beforeUpdate() {
    if (!String(useRouter().currentRoute.value.path).includes(this.isbn)) {
      this.upt = false;
    }
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
  justify-content: center;
  align-content: center;
  width: 100%;
}
.book-genders {
  display: block;
  width: 50%;
  color: black;
}
.author {
  display: inline-block;
  margin: 3px 8px;
}
.book-footer {
  display: flex;
  flex-direction: row;
  align-items: top;
  justify-content: space-between;
  margin: 1rem 1rem;
}
.book-chip {
  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: center;
  margin-bottom: 0.5rem;
}
.book-chip-text {
  margin-right: 1rem;
}
.book-resume {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 1rem 1rem;
  padding: 1rem 1.25rem;
  border: 1px solid rgba(238, 238, 238, 0.863);
  border-radius: 8px;
  h3 {
    font-size: 18pt;
    margin-bottom: 0.35rem;
  }
  p {
    font-weight: 500;
    text-align: justify;
  }
}
.book-resume:hover {
  background-color: rgba(255, 255, 255, 0.808);
}
</style>
