<template>
  <div>
    <div class="item-container" v-if="isbn.length > 0 && !loading" @click="goto()">
      <img :src="image" />
      <span class="item-title">{{ title }}</span>
      <span class="item-authors">{{ authors.join(", ") }}</span>
      <span class="item-genders">{{ genders.join(", ") }}</span>
      <span class="item-pages">{{ pages }}</span>
    </div>
    <div class="container-loading" v-else-if="isbn.length > 0">
      <va-progress-bar indeterminate />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import refreshToken from "../refresh";

export default {
  name: "SearchServiceOne",
  data() {
    return {
      isbn: "",
      loading: false,
    };
  },
  props: {
    title: String,
    authors: Array,
    image: String,
    genders: Array,
    pages: Number,
    all: Object,
  },
  methods: {
    goto() {
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
              gender: this.genders.length > 0 ? this.genders.join(", ") : "Undefined",
              author:
                this.authors !== undefined && this.authors.length > 0
                  ? this.authors.join(", ")
                  : "Undefined",
              formato:
                this.all.volumeInfo.printType !== undefined
                  ? this.all.volumeInfo.printType
                  : "Undefined",
              resume:
                this.all.volumeInfo.description !== undefined
                  ? this.all.volumeInfo.description
                  : this.all.searchInfo !== undefined
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
              this.$router.push({ path: "/book/" + this.isbn });
            })
            .catch((err) => {
              this.$router.push({ path: "/book/" + this.isbn });
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
  beforeRouteLeave(to, from, next) {
    this.$forceUpdate();
  },
};
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
.container-loading {
  display: block;
  padding: 4rem 2rem;
  width: 100%;
  height: 100%;
  align-items: center;
}
</style>
