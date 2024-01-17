<template>
    <div class="trust-bar">
      <div v-for="(logo, index) in logos" :key="index" class="trust-logo">
        <img :src="logo.src" :alt="logo.name" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TrustBar',
    data() {
      return {
        // Replace these with the path to your actual logo images
        logos: [
          { name: 'BenQ', src: 'src/assets/logos/benq.webp' },
          { name: 'Sony', src: 'src/assets/logos/sony.webp' },
          { name: 'Xerox', src: 'src/assets/logos/xerox.webp'},
          {name: 'HP', src: 'src/assets/logos/hp.webp'},
          {name: 'EPSON', src: 'src/assets/logos/epson.webp'},
          {name: 'Lenovo', src: 'src/assets/logos/lenovo.webp'},
          {name: 'Acer', src: 'src/assets/logos/acer.webp'},
          // ... add all logos here
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .trust-bar {
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: white; /* Or any other background */
  }
  
  .trust-logo img {
    /* filter: grayscale(100%); 
    transition: filter 0.3s ease; */
    height: 50px; /* Or your desired size */
  }
/*   
  .trust-logo img:hover {
    filter: none; 
  } */
  </style>
  