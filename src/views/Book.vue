<template>
  <div id="main">
    <div class="flex lg6 xs12 py-4" v-if="success === -1">
      <va-progress-circle indeterminate size="large" />
    </div>
    <div v-if="success === 1">Funciona Perro</div>
    <div v-if="success === 0">No funciona</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Book",
  props: {
    isbn: String,
  },
  data() {
    return {
      book: {},
      success: -1,
    };
  },
  created() {
    let body = {
      filters: [
        {
          option: "ISBN",
          value: this.$route.params.isbn,
        },
      ],
    };
    console.log(this.$route.params);
    axios
      .post("http://localhost:8000/get-book/", body)
      .then((response) => {
        console.log(response);
        this.book = response.data;
        this.success = 1;
      })
      .catch((error) => {
        this.success = 0;
      });
  },
};
</script>

<style lang="scss">
#main2 {
  display: flex;
  align-content: center;
  text-align: center;
  align-items: center;
  min-width: 720px;
  min-height: 100%;
  div {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
