<template>
  <div v-for="item in comments" :key="item.id">
    {{ item.comment }}
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "Comments",
  props: {
    isbn: String
  },
  data() {
    return {
      comments: []
    }
  },
  beforeCreate() {
    let url = process.env.VUE_APP_BACK_END_URL + "comment/?isbn=" + this.isbn;
    axios.get(url).then(response => {
      this.comments = response.data.result;
      console.log(this.comments);
    }).catch(error => { })
  },
}
</script>

<style>
</style>