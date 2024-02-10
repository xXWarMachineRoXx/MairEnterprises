<template>
  <div class="flex flex-wrap gap-4 lg:gap-6 lg:flex-nowrap justify-center pb-20">
    <div
      v-for="({ image, title, backgroundColor }, index) in cardDetails"
      :key="`${title}-${index}`"
      class="flex flex-col min-w-[325px] max-w-[375px] lg:w-[496px] relative border border-neutral-200 rounded-md hover:shadow-xl md:items-center"
      :class="backgroundColor" 
    >
      <a
        class="absolute inset-0 z-1 focus-visible:outline focus-visible:outline-offset focus-visible:rounded-md"
        href="#"
      ></a>
      <img :src="image" :alt="title" class="object-cover h-auto rounded-t-md aspect-video" />
      <div class="flex flex-col items-start p-4 grow text-center">
        <p class="font-medium typography-text-base">{{ title }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import stock from '@/assets/images/hjjj-500x500.webp'
import board from '@/assets/images/bbbb-500x500.webp'
import production from '@/assets/images/gggh-500x500.webp'

const cardDetails = [
  {
    image: stock,
    title: 'Product Packaging',
    backgroundColor: 'bg-primary-200', 
  },
  {
    image: board,
    title: 'Our Board Image ',
    backgroundColor: 'bg-secondary-200', 
  },
  {
    image: production,
    title: 'Production Facility',
    backgroundColor: 'bg-primary-200', 
  },
];
</script>
