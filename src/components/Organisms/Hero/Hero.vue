<template>
  <div class="relative min-h-[600px] bg-gradient-to-l from-primary-100">
    <!-- <picture>
        <source :srcset="HeroBackground" />
        <img
          :src="HeroBackground"
          class="absolute w-full h-full z-[-1] md:object-cover"
          alt="hero"
        />
      </picture> -->
    <div class="md:flex md:flex-row-reverse md:justify-center max-w[1536px] mx-auto md:min-h-[600px]">
      <div class="flex flex-col md:basis-2/4 md:items-stretch md:overflow-hidden">
        <img :src="HeroImage" alt="BenQ TK700" class="h-full object-cover object-left" />
      </div>
      <div
        class="p-4 md:p-10 md:max-w-[768px] md:flex md:flex-col md:justify-center md:items-start md:basis-2/4 prose lg:prose-xl">
        <p class="typography-text-xs md:typography-text-sm font-bold tracking-widest uppercase">
          IMMERSE IN CINEMA 
        </p>
        <h1 class="p md:typography-display-1 md:leading-[67.5px] font-bold mt-2 mb-2 text-xl md:text-4xl">
          BenQ EH600 Smart Projector
        </h1>
        <p class="typography-text-base md:typography-text-lg">
          Crisp 4K Visuals, Intuitive Controls, Endless Entertainment.
        </p>


        <div class="flex flex-col md:flex-row gap-4 mt-6">
          <SfButton size="lg" class="bg-primary-300"> Order now </SfButton>
          <SfButton size="lg" variant="secondary" class=" text-primary-500 "> Show more </SfButton>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';

const HeroImage = 'src/assets/images/benq.png';
// const HeroBackground='src/assets/images/hero-bg.webp'
</script>
  