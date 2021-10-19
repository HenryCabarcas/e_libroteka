<template>
  <div id="main">
    <div id="container" class="blur">
      <h1>Register Book</h1>
      <div id="fields">
        <va-input
          class="mb-4"
          v-model="title"
          :rules="[(title) => title.length >= 2 || `Please insert a book title.`]"
          label="Title"
          placeholder="Book title"
        />
        <va-input
          class="mb-4"
          v-model="isbn"
          :messages="ISBNmessage"
          :rules="[
            (isbn) =>
              isbn.length == 10 || isbn.length == 13 || `The ISBN number is invalid.`,
          ]"
          label="ISBN"
          placeholder="Book ISBN"
        />
        <va-slider
          class="mb-4"
          id="volume-slider"
          v-model="volume"
          max="15"
          min="1"
          label="Volume"
          track-label-visible
        >
        </va-slider>
        <va-input
          class="mb-4"
          v-model="editorial"
          label="Editorial"
          placeholder="Book editorial."
        />
        <va-select
          class="mb-4"
          label="Select book gender/s"
          :options="genderList"
          v-model="gender"
          multiple
          searchable
        />

        <va-select
          class="mb-4"
          label="Select book format"
          v-model="format"
          :options="formatList"
        />
        <va-input class="mb-4" v-model="url" label="Url" placeholder="Book url." />
        <va-input
          class="mb-4"
          v-model="resume"
          type="textarea"
          label="Resume"
          placeholder="Book Resume"
          :rules="[
            (resume) =>
              resume.length <= 500 || `The maximum length of characters is 500.`,
          ]"
        />
      </div>
      <div id="buttons" class="mb-2">
        <va-button color="info" gradient class="mr-4" @click="registerBook($vaToast)"
          >Register</va-button
        >
        <va-button color="danger" gradient class="mr-4">Cancel</va-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterBook",
  data() {
    return {
      title: "",
      isbn: "",
      volume: 1,
      editorial: "",
      gender: "",
      format: "any",
      resume: "",
      url: "",
      ISBNmessage: "Insert a number.",
      formatList: ["any", "pdf", "e-book", "web page", "audiobook"],
      genderList: [
        "romance",
        "fiction",
        "young-adult",
        "fantasy",
        "science-fiction",
        "non-fiction",
        "children",
        "history",
        "covers",
        "mystery",
        "best",
        "horror",
        "historical-fiction",
        "gay",
        "paranormal",
        "love",
        "titles",
        "historical-romance",
        "middle-grade",
        "biography",
        "thriller",
        "contemporary",
        "women",
        "nonfiction",
        "graphic-novels",
        "classics",
        "series",
        "lgbt",
        "memoir",
        "queer ,",
      ],
      volumeMax: 15,
      volumeMin: 1,
    };
  },
  methods: {
    registerBook(vaToast) {
      if ((this.isbn.length == 10 || this.isbn.length == 13) && this.title.length > 0) {
        let body = {
          book: {
            ISBN: this.isbn,
            title: this.title,
            volume: this.volume > 0 ? String.toString(this.volume) : "1",
            gender: this.gender.length > 0 ? this.gender : "Any",
            editorial: this.editorial.length > 0 ? this.editorial : "Any",
            format: this.format.length > 0 ? this.format : "Any",
            resume: this.resume.length > 0 ? this.resume : "Any",
            url: this.url.length > 0 ? this.url : null,
          },
        };
        axios
          .post("http://localhost:8000/post-book/", body)
          .then((response) => {
            console.log(response.data);
            this.message = response.data;
            vaToast.init({
              message: "The book was successfully registered",
              color: "success",
            });
          })
          .catch((response) => {
            console.log(response);
            vaToast.init({
              message: "The book cannot be registered",
              color: "danger",
            });
          });
      } else {
        vaToast.init({
          message: "Please verify the filled data.",
          color: "danger",
        });
      }
    },
    verifyVolume() {
      if (this.volume < 0) this.volume = 0;
      if (this.volume > 15) this.volume = 15;
    },
  },
};
</script>

<style lang="scss">
#main {
  display: block;
  align-content: center;
  text-align: center;
  align-items: center;
  padding: 10%;
}
#container {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-self: center;
  max-width: 1000px;
  box-shadow: 20px 20px 40px #c2c2c2, -20px -20px 40px #ffffff;
  border-radius: 12px;
  margin-left: auto;
  margin-right: auto;
}
#fields {
  width: 100%;
  padding: 5%;
  margin-left: 10px;
  margin-right: 10px;
}
#volume-slider {
  display: flex;
  align-content: stretch;
  padding-left: 10px;
  padding-right: 0;
}
h1 {
  font-size: 24pt;
}
</style>
