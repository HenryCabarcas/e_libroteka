<template>
  <div class="comment-container">
    <div class="comment-header">
      <span>
        <va-avatar size="1.2rem" class="mr-4">{{ info.user[0] }}</va-avatar>
      </span>
      <span class="user-name">{{ info.user }}</span>
      <span class="comment-score">
        Score:
        <va-rating v-model="info.score" color="warning" readonly size="small"
      /></span>
    </div>
    <div class="comment-body">
      <div class="comment-content">{{ info.comment }}</div>
      <div class="comment-creation">{{ this.date }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Comment",
  components: {},
  props: {
    info: Object,
  },
  data() {
    let dt = this.info.creationDate; //new Date(this.info.creationDate.substring(0, this.info.creationDate.length - 2));
    let date = dt.toDateString() + " - " + dt.toLocaleTimeString();
    return {
      date: date,
    };
  },
};
</script>

<style lang="scss">
.comment-container {
  display: block;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 4px;
  background-color: white;
  border-radius: 6px;
  border: 1px rgba(206, 206, 206, 0.568) solid;
  overflow: hidden;
}
.comment-container:hover {
  box-shadow: 1px 0px 3px 1px rgba(56, 56, 56, 0.342);
}
.comment-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 1rem;
  border-bottom: 1px solid rgba(187, 187, 187, 0.616);
}
.comment-score {
  display: flex;
  flex-direction: row;
  font-size: 11pt;
  color: rgba(0, 0, 0, 0.25);
  align-self: flex-end;
  flex: 0;
}
.user-name {
  color: rgb(41, 41, 41);
  font-weight: 600;
  width: 100%;
  text-align: left;
}
.comment-body {
  display: block;
  padding: 0.2rem;
}
.comment-content {
  display: block;
  padding: 0.45rem 0.1rem;
  text-overflow: ellipsis;
  align-content: left;
  font-size: 11pt;
  color: rgb(58, 58, 58);
  text-align: left;
}
.comment-creation {
  display: block;
  text-align: right;
  color: rgb(165, 165, 165);
  font-size: 9pt;
}
</style>
