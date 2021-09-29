<template>
  <div>
    Hej Nexer
    <button @click="test()">Test</button>
    {{message}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data: function() {
    return {
      message: "hello"
    }
  },
  methods: {
    test() {
      fetch("posts.json").then((response) => {
        response.json().then((data) => {
          this.message = JSON.stringify(data[0]);
        }
      )})
    }
  }
}
</script>

<style>
</style>
