<template>
    <div>
      <h1>Products</h1>
      <ul>
        <li v-for="product in products" :key="product.id">
          <router-link :to="'/products/' + product.id">{{ product.name }}</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: [
          { id: 1, name: 'Product 1' },
          { id: 2, name: 'Product 2' },
          { id: 3, name: 'Product 3' },
          // Add more products here as needed
        ]
      };
    }
  };
  </script>
  