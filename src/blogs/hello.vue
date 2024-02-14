<template>
  <div class="blog">
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
    <div v-for="comment in comments" :key="comment.id">
      <p>{{ comment.text }}</p>
      <p>By: {{ comment.author }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Hello Blog",
      content: "Welcome to my blog!",
      comments: [
        { id: 1, text: "Great post!", author: "John" },
        { id: 2, text: "I enjoyed reading this.", author: "Jane" },
      ],
    };
  },
};
</script>

<style scoped>
.blog {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
