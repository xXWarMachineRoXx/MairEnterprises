<template>
  <div class="bg-secondary-100">
    <!-- <h1 class="text-center text-5xl font-bold mt-10 mb-5 !bg-primary-100">Trusted Brand Channel Partners</h1> -->
    <div class="trust-bar ">
      <div v-for="(logo, index) in logos" :key="index" class="trust-logo">
        <img :src="logo.src" :alt="logo.name" />
      </div>
    </div>
  </div>
</template>
  
<script>
import BenQ from '@/assets/logos/benq.webp';
import Sony from '@/assets/logos/sony.webp';
import Xerox from '@/assets/logos/xerox.webp';
import HP from '@/assets/logos/hp.webp';
import EPSON from '@/assets/logos/EPSON.png';
import Lenovo from '@/assets/logos/lenovo.webp';
import Acer from '@/assets/logos/acer.png';

export default {
  name: 'TrustBar',
  data() {
    return {
      // Replace these with the path to your actual logo images
      logos: [
        { name: 'BenQ', src: BenQ },
        { name: 'Sony', src: Sony },
        { name: 'Xerox', src: Xerox },
        { name: 'HP', src: HP },
        { name: 'EPSON', src: EPSON },
        { name: 'Lenovo', src: Lenovo },
        { name: 'Acer', src: Acer },
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
  
  /* Or any other background */
}

.trust-logo img {
  /* filter: grayscale(100%); 
    transition: filter 0.3s ease; */
  height: 50px;
  /* Or your desired size */
}

/*   
  .trust-logo img:hover {
    filter: none; 
  } */</style>
  