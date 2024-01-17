<template>
  
    <TopBar class="!bg-primary-300 !text-primary-800" />
  
    <NavbarVue class="!bg-primary-50 "/>
    <Hero/>
    <FeatureBanner/>
    <h1 class="text-center text-4xl font-bold mt-10">Projectors</h1>
    <ProductSlider :products="Projectors" class="mt-6 w-full"/>
    <h1 class="text-center text-4xl font-bold mt-10">Home Theaters</h1>
    <ProductSlider class="mt-6 w-full"/>
    
    <h1 class="text-center text-5xl font-bold mt-10">Trusted Brand Channel Partners</h1>
    <TrustBanner class="mt-20"/>
    
  
    <Footer class="mt-20"></Footer>
  </template>
  
  <script lang="ts" setup>
  import {ref} from 'vue';

  import NavbarVue from '../components/Organisms/Navbar/Navbar.vue';
  import TopBar from '../components/Organisms/Topbar/TopBar.vue';
  import Hero from '../components/Organisms/Hero/Hero.vue';
  import FeatureBanner from '../components/Organisms/FeatureBanner/FeatureBanner.vue';
  // import Newsletter from './components/Organisms/NewsLetter/Newsletter.vue';
  // import BestSeller from './components/Organisms/BestSeller/BestSeller.vue';
  import ProductSlider from '../components/Organisms/ProductSlider/ProductSlider.vue';
  import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
  import Footer from '../components/Organisms/Footer/Footer.vue';
  

  const Projectors = ref([
  {
    id: 1,
    name: 'BenQ EH600 Smart Projector',
    price: '₹ 74,899',
    img: {
      src: 'src/assets/images/benq.png',
      alt: 'BenQ Projector',
    },
  },
  
  {
    id: 2,
    name: 'EGate K9 Pro Max Android Projector',
    price: '₹ 74,899',
    img: {
      src: 'src/assets/images/products/egate-k9-pro-max-android-projector-500x500.webp',
      alt: 'BenQ Projector',
    },
  },
  {
    id: 1,
    name: 'EGATE L9 Pro Android Projector',
    price: '₹ 74,899',
    img: {
      src: 'src/assets/images/benq.png',
      alt: 'BenQ Projector',
    },
  },
  {
    id: 1,
    name: 'BenQ EH600 Smart Projector',
    price: '₹ 74,899',
    img: {
      src: 'src/assets/images/benq.png',
      alt: 'BenQ Projector',
    },
  },
  {
    id: 2,
    name: 'EGATE I9 Pro Max Android Projector',
    price: '₹ 74,899',
    img: {
      src: 'src/assets/images/products/EGATE-I9-Pro-Max-Android-Projector.webp',
      alt: 'BenQ Projector',
    },
  },
]);



</script>