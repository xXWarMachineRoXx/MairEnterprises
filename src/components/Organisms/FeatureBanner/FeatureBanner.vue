<template>
  <div class="flex flex-col gap-6 md:flex-row">
    <div class="flex flex-col gap-6 md:flex-row">
      <div v-for="{ title, subtitle, description, callToAction, image, backgroundColor, reverse,link } in displayDetails"
        :key="title" :class="[
          `relative flex flex-col justify-between rounded-md md:items-center md:basis-1/2 ${backgroundColor} hover:shadow-md`,
          { 'flex-col-reverse': reverse },
        ]">
        <router-link :to="link"
          class="prose lg:prose-xl absolute w-full h-full z-1 focus-visible:outline focus-visible:rounded-lg"
          :aria-label="title" />
        <div class="flex flex-col p-4 text-center md:p-10">
          <p class="mb-2 font-bold tracking-widest uppercase typography-headline-6">{{ subtitle }}</p>
          <p class="mb-4 font-bold text-xl">{{ title }}</p>
          <p class="mb-4 text-lg">{{ description }}</p>
          <router-link :to="{ path: '/products' }" tag="div" class="w-full z-10">
            <SfButton class="font-semibold !bg-primary-50 !text-primary-700 hover:!bg-primary-800 hover:!text-primary-50">
              {{ callToAction }}
            </SfButton>
          </router-link>
        </div>
        <div class="flex items-center w-full p-2 mt-10">
          <img :src="image" :alt="title" class="w-full" />
        </div>
      </div>
    </div>
  </div>
</template>
  
<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import homeTheater from '@/assets/images/home-theater.png';
import workanywhere from '@/assets/images/work-anywhere.png';
import networkCamera from '@/assets/images/network-camera.png';
import smartboard from '@/assets/images/products/smart-board.webp';
// src/assets/images/products/smart=board.webp

const displayDetails = [
  {
    title: 'Power Your Work',
    subtitle: 'Unleash Productivity',
    description: 'Explore our range of high-performance desktops',
    callToAction: 'Find Your Desktop',
    image: homeTheater,
    backgroundColor: 'bg-primary-300',
    reverse: true,
    link: '/products',
  },
  {
    title: 'Mobility Meets Performance',
    subtitle: 'Work Anywhere',
    description: 'Discover our versatile laptop collection for professionals on the move',
    callToAction: 'Browse Laptops',
    image: workanywhere,
    backgroundColor: 'bg-secondary-100',
    reverse: true,
    link: '/products',
  },


  {
  title: 'Smart Displays for Smarter Living',
  subtitle: 'Enhance Your Home Experience',
  description: 'Discover our innovative smart displays designed to make your daily life easier and more connected',
  callToAction: 'Shop Smart Displays',
  image: smartboard,
  backgroundColor: 'bg-secondary-100',
  reverse: true,
  link: 'blog/benq-65-inch-interactive-panel',
},
  {
    title: 'Stay Connected',
    subtitle: 'Reliable Networking Solutions',
    description: 'Efficient and secure IT networking products to keep you connected',
    callToAction: 'Explore Networking Solutions',
    image: networkCamera,
    backgroundColor: 'bg-primary-300',
    reverse: true,
    link: '/products',
  },

];
</script>
  