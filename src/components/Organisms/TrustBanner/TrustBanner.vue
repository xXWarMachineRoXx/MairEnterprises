<template>
  <div class="bg-secondary-100 ">
    <!-- <h1 class="text-center text-5xl font-bold mt-10 mb-5 !bg-primary-100">Trusted Brand Channel Partners</h1> -->
    <div class="trust-bar trust-bar-wrapper">
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

.trust-bar-wrapper {
  overflow-x: auto; /* Enables horizontal scrolling */
  overflow-y: hidden; /* Hides vertical scrollbar */
  -webkit-overflow-scrolling: touch; /* Smooth scrolling on touch devices */
  scrollbar-width: none; /* For Firefox */
  -ms-overflow-style: none;  /* For Internet Explorer and Edge */
}

.trust-bar-wrapper::-webkit-scrollbar {
  display: none; /* For Chrome, Safari, and Opera */
}

.trust-bar {
  display: flex;
  flex-wrap: nowrap; /* Ensures logos stay in a single line and do not wrap */
  overflow-x: auto; /* Enables horizontal scrolling */
  align-items: center;
  justify-content: space-between; /* Align items from the according to space avaiable */
  padding: 10px 0; /* Adds some padding top and bottom */
  gap: 20px; /* Adds space between logos */
}

.trust-logo {
  flex: 0 0 auto; /* Do not grow, do not shrink, and be automatically sized by content */
  display: flex; /* Use flexbox for alignment */
  align-items: center; /* Center-align the logo vertically */
}

.trust-logo img {
  max-height: 50px; /* Set a maximum height for logos */
  width: auto; /* Adjust width automatically to maintain aspect ratio */
}

</style>
  