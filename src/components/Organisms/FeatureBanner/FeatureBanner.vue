<template>
    <div class="flex flex-col gap-6 md:flex-row">
      <div class="flex flex-col gap-6 md:flex-row">
        <div
          v-for="{ title, subtitle, description, callToAction, image, backgroundColor, reverse } in displayDetails"
          :key="title"
          :class="[
            `relative flex flex-col justify-between rounded-md md:items-center md:basis-1/2 ${backgroundColor}`,
            { 'flex-col-reverse': reverse },
          ]"
        >
          <a
            class="prose lg:prose-xl absolute w-full h-full z-1 focus-visible:outline focus-visible:rounded-lg"
            :aria-label="title"
            href="#"
          />
          <div class="flex flex-col p-4 text-center md:p-10">
            <p class="mb-2 font-bold tracking-widest uppercase typography-headline-6">{{ subtitle }}</p>
            <p class="mb-4 font-bold text-xl">{{ title }}</p>
            <p class="mb-4 text-lg">{{ description }}</p>
            <SfButton class="font-semibold !bg-primary-50 !text-primary-700 hover:!bg-primary-800 hover:!text-primary-50 z-10">
              {{ callToAction }}
            </SfButton>
          </div>
          <div class="flex items-center w-full">
            <img :src="image" :alt="title" class="w-full" />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { SfButton } from '@storefront-ui/vue';
  
  const displayDetails = [
    {
      title: 'Power Your Work',
      subtitle: 'Unleash Productivity',
      description: 'Explore our range of high-performance desktops',
      callToAction: 'Find Your Desktop',
      image: 'src/assets/images/home-theater.png',
      backgroundColor: 'bg-primary-300',
      reverse: true,
    },
    {
      title: 'Mobility Meets Performance',
      subtitle: 'Work Anywhere',
      description: 'Discover our versatile laptop collection for professionals on the move',
      callToAction: 'Browse Laptops',
      image: 'src/assets/images/work-anywhere.png',
      backgroundColor: 'bg-secondary-100',
      reverse: true,
    },
  
    
    {
      title: 'Power Your Work',
      subtitle: 'Unleash Productivity',
      description: 'Explore our range of high-performance desktops',
      callToAction: 'Find Your Desktop',
      image: 'src/assets/images/power-your-work.png',
      backgroundColor: 'bg-secondary-100',
      reverse: true,
    },
    {
      title: 'Stay Connected',
      subtitle: 'Reliable Networking Solutions',
      description: 'Efficient and secure IT networking products to keep you connected',
      callToAction: 'Explore Networking Solutions',
      image: 'src/assets/images/network-camera.png',
      backgroundColor: 'bg-primary-300',
      reverse: true,
    },
    
  ];
  </script>
  