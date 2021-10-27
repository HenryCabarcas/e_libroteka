<template>
  <div class="comments" id="comments">
    <div class="clear comment-input">
      <h1 class="comments-title">Comments</h1>
    </div>
    <div class="comment-input">
      <va-input
        v-model="newComment"
        placeholder="Comment about this book..."
        type="textarea"
        @input="commentLimit()"
      />
      <div class="new-comment-footer" v-if="newComment.length > 2">
        <div>
          <va-rating v-model="score" color="warning" />
        </div>
        <div class="add-comment-btns">
          <va-button color="info" @click="promptUser()" style="margin-right: 5px"
            >Comment</va-button
          >
          <va-button color="danger" @click="clearComment()" flat>Cancel</va-button>
        </div>
      </div>
    </div>
    <div>
      <Comment :info="item" v-for="item in comments" :key="item.id"> </Comment>
    </div>
  </div>
  <va-modal v-model="showModal" hide-default-actions overlay-opacity="0.2" size="medium">
    <template #header>
      <h2>User info</h2>
    </template>
    <slot>
      <div class="modal-comment">
        <p class="mb-4">Please insert an username and a email direction</p>
        <va-input
          v-model="username"
          placeholder="Username"
          type="text"
          @input="validateInfo()"
          label="Username"
          class="mb-4"
          :success="validUsername == 1"
          :error="validUsername == -1"
        />
        <va-input
          v-model="email"
          placeholder="Email"
          type="email"
          @input="validateInfo()"
          label="E-mail"
          :success="validEmail == 1"
          :error="validEmail == -1"
        />
      </div>
    </slot>
    <template #footer>
      <div class="add-comment-btns modal-foot">
        <va-button
          color="info"
          @click="setUser($vaToast)"
          style="margin-right: 5px"
          :loading="settingUser"
          >Accept & Submit</va-button
        >
        <va-button color="danger" flat @click="hideModal()">Cancel</va-button>
      </div>
    </template>
  </va-modal>
</template>

<script>
import Comment from "./Comment.vue";
import axios from "axios";
import refreshToken from "../refresh";

export default {
  name: "Comments",
  components: {
    Comment,
  },
  props: {
    isbn: String,
  },
  data() {
    return {
      comments: [],
      newComment: "",
      score: 0,
      showModal: false,
      username: "",
      email: "",
      settingUser: false,
      canSetUser: false,
      validUsername: 0,
      validEmail: 0,
    };
  },

  beforeMount() {
    this.getComments();
  },
  methods: {
    getComments() {
      let url = process.env.VUE_APP_BACK_END_URL + "comment/?isbn=" + this.isbn;
      axios
        .get(url)
        .then((response) => {
          this.comments = response.data.result.map((value) => {
            value.creationDate = new Date(
              value.creationDate.substring(0, value.creationDate.length - 2)
            );
            return value;
          });
          this.comments = this.comments.sort(
            (a, b) => b.creationDate.getTime() - a.creationDate.getTime()
          );
        })
        .catch((error) => {});
    },
    commentLimit() {
      if (this.newComment.length >= 500)
        this.newComment = this.newComment.substring(0, 499);
    },
    validateInfo() {
      if (this.username.length >= 20) this.username = this.username.substring(0, 19);
      if (this.validateEmail(this.email)) this.validEmail = 1;
      else this.validEmail = -1;
      if (this.username.length >= 3 && this.validateEmail(this.email))
        this.canSetUser = true;
      if (this.username.length >= 3) this.validUsername = 1;
      else this.validUsername = -1;
    },
    validateEmail(elementValue) {
      var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      return emailPattern.test(elementValue);
    },
    clearComment() {
      this.newComment = "";
      this.score = 0;
    },
    submitComment(toast) {
      let done = (ms, success) => {
        this.settingUser = false;
        this.showModal = false;
        toast.init({ message: ms, color: success ? "success" : "danger" });
        this.getComments();
        this.clearComment();
      };

      let url = process.env.VUE_APP_BACK_END_URL + "comment/";
      const body = {
        comment: {
          book: this.isbn,
          score: this.score,
          comment: this.newComment,
          user: this.username,
        },
      };
      refreshToken().then((res) => {
        const config = {
          headers: {
            "Content-type": "application/json",
            Authorization: `Bearer ${window.localStorage.getItem("access_token")}`,
          },
        };
        axios
          .post(url, body, config)
          .then((response) => {
            done("The comment was submitted.", true);
          })
          .catch((error) => {
            done("The comment cannot be submitted." + String(error), false);
          });
      });
    },
    setUser(toast) {
      if (!this.canSetUser) {
        toast.init({
          message: "Please insert a valid username and email.",
          color: "warning",
        });
      } else {
        this.settingUser = true;
        let url = process.env.VUE_APP_BACK_END_URL + "register/";
        let pwd = process.env.VUE_APP_ANY_USER_PWD;
        window.localStorage.setItem("username", this.username);
        window.localStorage.setItem("email", this.email);
        const body = {
          username: this.username,
          password: pwd,
          email: this.email,
        };
        axios
          .post(url, body)
          .then((response) => {
            this.submitComment(toast);
          })
          .catch((error) => {
            toast.init({
              message: "This username or email is taken, so we'll use the database info.",
              color: "warning",
            });
            this.submitComment(toast);
          });
      }
    },
    promptUser() {
      this.showModal = true;
      if (window.localStorage.getItem("username") !== null) {
        this.username = window.localStorage.getItem("username");
        this.validateInfo();
      }
      if (window.localStorage.getItem("email") !== null) {
        this.email = window.localStorage.getItem("email");
        this.validateInfo();
      }
    },
    hideModal() {
      this.showModal = false;
      this.email = "";
      this.username = "";
    },
  },
};
</script>

<style lasng="scss">
.comments {
  display: block;
  margin: 1rem 1rem;
  padding: 1rem 1.25rem;
  background-color: rgba(255, 255, 255, 0.739);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 12px;
  text-align: left;
}
.comment-input {
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
.comments-title {
  font-size: 18pt;
}
.add-comment-btns {
  display: flex;
  padding: 0.25rem;
  justify-content: flex-end;
}
.new-comment-footer {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.modal-comment {
  display: block;
  padding: 1rem 1rem;
}
.modal-foot {
  border-top: 1px solid rgba(167, 167, 167, 0.246);
  width: 100%;
}
.clear {
  background-color: transparent;
  border: none;
}
</style>
