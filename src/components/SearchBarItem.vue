<template>
  <div class="sresult-container" @click="goto()" v-if="isbn.length > 0 && !loading">
    <span class="sresult-title">
      {{ title }}
    </span>
    <span class="sresult-author" v-if="author.length > 1">
      {{ author }}
    </span>
  </div>
  <div class="scontainer-loading" v-else-if="isbn.length > 0">
    <va-progress-bar indeterminate />
  </div>
</template>

<script>
import axios from "axios";
import refreshToken from "../refresh";
export default {
  name: "SearchBarItem",
  props: {
    title: String,
    author: String,
    all: Object,
  },
  data() {
    return {
      isbn: "",
      show: true,
      loading: false,
    };
  },
  emits: ["update:show"],
  methods: {
    goto() {
      console.log("peticion");
      if (!this.loading) {
        this.loading = true;

        refreshToken().then((result) => {
          const body = {
            book: {
              ISBN: this.isbn,
              title: this.title,
              publicationDate:
                this.all.volumeInfo.publishedDate !== undefined
                  ? this.all.volumeInfo.publishedDate.substr(0, 4)
                  : "0000",
              gender: this.all.volumeInfo.categories
                ? this.all.volumeInfo.categories.join(", ")
                : "Undefined",
              author:
                this.author !== undefined && this.author.length > 0
                  ? this.author
                  : "Undefined",
              formato:
                this.all.volumeInfo.printType !== undefined
                  ? this.all.volumeInfo.printType
                  : "Undefined",
              resume:
                this.all.volumeInfo.description !== undefined
                  ? this.all.volumeInfo.description
                  : this.all.searchInfo.textSnippet !== undefined
                  ? this.all.searchInfo.textSnippet
                  : "...",
              url:
                this.all.volumeInfo.imageLinks.thumbnail !== undefined
                  ? this.all.volumeInfo.imageLinks.thumbnail
                  : this.all.volumeInfo.imageLinks.smallThumbnail !== undefined
                  ? this.all.volumeInfo.imageLinks.smallThumbnail
                  : null,
              pages: Number(this.all.volumeInfo.pageCount),
            },
          };
          const config = {
            headers: {
              "Content-type": "application/json",
              Authorization: `Bearer ${window.localStorage.getItem("access_token")}`,
            },
          };
          let url = process.env.VUE_APP_BACK_END_URL + "book/";
          axios
            .post(url, body, config)
            .then((response) => {
              console.log(response.data);
              this.$emit("update:show", false);
              this.$router.push("/book/" + this.isbn);
            })
            .catch((err) => {
              this.$emit("update:show", false);
              this.$router.push("/book/" + this.isbn);
            });
        });
      }
    },
  },
  beforeMount() {
    let isbns = this.all.volumeInfo.industryIdentifiers;
    if (isbns !== undefined) {
      let isbnsValues = Array(
        isbns.map((item) => {
          let val = String(item.identifier).matchAll("\\d+").next().value;
          return val ? val[0] : "";
        })
      );
      this.isbn = isbnsValues.sort((a, b) => a.length - b.length)[0][0];
      if (this.isbn.length < 6 || this.isbn.length > 20) this.isbn = "";
    }
  },
};
</script>

<style>
.sresult-container {
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
  overflow: hidden;
}
.sresult-container:hover {
  background-color: rgba(0, 0, 0, 0.15);
}
.sresult-container * span {
  display: block;
  text-align: left;
  align-items: flex-start;
  justify-content: center;
  max-width: 50%;
}
.sresult-title {
  font-weight: 600;
  grid-column-start: 1;
  grid-column-end: 2;
  padding: 0 1rem;
  margin: 2px 8px;
}
.sresult-author {
  color: gray;
  grid-column-start: 2;
  grid-column-end: 3;
}
.scontainer-loading {
  padding: 1.2rem;
}
</style>
