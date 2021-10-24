<template>
  <div class="about">
    <Comments isbn="1000000011229"></Comments>
    <h1>This is an about page</h1>
  </div>
</template>

<script>
import Comments from "@/components/Comments.vue"
export default {
  name: "About",
  components: {
    Comments
  }
}
</script>
