<template>
  <div class="posts">
    <div class="newPost">
      <label for="newPost">New Post</label><br>
      <input id="name" type="text" v-model="name"><br>
      <input id="newPost" type="text" v-model="newMessage"><br>
      <button @click="addPost(newMessage)">Post</button><br><br>
    </div>
    <div class="post" v-for="(post, index) in posts" :key="index">
      <strong>{{post.user}}</strong><br>
      {{post.message}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostViewer',
  data: function() {
    return {
      posts: [],
      name: 'David',
      newMessage: '',
      loading: false
    }
  },
  mounted() {
    this.loadPosts();
  },
  methods: {
    loadPosts() {
      fetch("messages.json").then((response) => {
        response.json().then((data) => {
          this.posts = data;
          this.loading = false;
        }
      )})
    },
    addPost(message) {
      this.loading = true;
      this.posts.push({
        user: this.name,
        message: message
      });
      /*fetch("https://1bbaga5v92.execute-api.eu-north-1.amazonaws.com/default/Nexertest", {
        method: 'POST',
        body: JSON.stringify({
          user: this.name,
          message: message
        })
      }).then(() => {
        this.loading = false;
      }).catch((e) => {
        this.loading = false;
        console.error(e);
      }).finally(() => {
        this.newMessage="";
        this.loadPosts();
      });*/
    }
  }
}
</script>

<style scoped>

  .newPost {
    margin: auto;
    width: 30vw;
    border: 1px solid #000;
  }
  .newPost label {
    font-weight: bold;
  }
  .newPost button {
    border-radius: 20px;
    border: 1px solid blue;
    background-color: white;
    margin: 4px;
    padding: 12px;
    padding-top: 6px;
    padding-bottom: 6px;
  }
  .newPost button:hover {
    background-color: #ccf;
  }
  .newPost button:active {
    background-color: #77f;
  }

  .post {
    margin: auto;
    margin-top: 20px;
    width: 30vw;
    border-radius: 10px;
    border: 1px solid red;
  }
</style>
