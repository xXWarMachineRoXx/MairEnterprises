<template>
  <TopBar />
  <Navbar />
  <navbarBottom class="md:hidden lg:hidden sm:hidden"/>
  <div class="mx-12 my-8 p-4">
    <Breadcrumbs />
    <div class="text-center">
      <h1 class="font-bold text-4xl">Our Blog</h1>
      <p class="text-lg">🔥Latest scoops, guides and trends in the world of electronics.</p>

    </div>
    <div class="flex justify-center mt-5">
      <BlogGallery />
    </div>
    
  </div>
  <TrustBanner />
  <Footer />
</template>
  
<script setup lang="ts">
import TopBar from '../components/Organisms/Topbar/TopBar.vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import BlogGallery from '../components/Organisms/BlogGallery/BlogGallery.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
import navbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';
import { useMeta } from 'vue-meta';

useMeta({
    title: 'Blog'
})
</script>
  