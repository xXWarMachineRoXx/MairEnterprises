<template>
  <div class="flex flex-wrap gap-4 lg:gap-6 lg:flex-nowrap">
    <div
      v-for="({ image, title, description, button, blogName }, index) in cardDetails"
      :key="`${title}-${index}`"
      class="flex flex-col min-w-[325px] max-w-[375px] lg:w-[496px] relative border border-neutral-200 rounded-md hover:shadow-xl"
    >
      <a
        class="absolute inset-0 z-1 focus-visible:outline focus-visible:outline-offset focus-visible:rounded-md"
        :href="`/blog/${blogName}`"
      ></a>
      <img :src="image" :alt="title" class="object-cover h-auto rounded-t-md aspect-video" />
      <div class="flex flex-col items-start p-4 grow">
        <p class="font-medium typography-text-base">{{ title }}</p>
        <p class="mt-1 mb-4 font-normal typography-text-sm text-neutral-700">{{ description }}</p>
        <SfButton @click="$router.push(`/blog/${blogName}`)" size="sm" variant="tertiary" class="relative mt-auto">{{ button }}</SfButton>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import workplaceTrends from '@/assets/images/blog/workplace.png'
import beforeYouBuy from '@/assets/images/blog/before-your-buy.png';
import workanywhere from '@/assets/images/work-anywhere.png';
import smartBoard from '@/assets/images/products/benq-smart-board.png';


const cardDetails = [
  {
    image: workplaceTrends,
    title: 'Benq predicts new work trends for 2024',
    description: '2024 is a year of change and innovation. BenQ predicts the new work trends that will shape the future of work.',
    button: 'Read more',
    blogName: 'benq-predicts-new-work-trends-for-2024'
  },
  {
    image: beforeYouBuy,
    title: 'Before you buy: Projector buying guide 2024',
    description: 'A comprehensive guide to help you choose the right projector for your home or office.',
    button: 'Read more',
    blogName: 'projector-buying-guide-2024'
  },
  {
    image: workanywhere,
    title: 'Best Laptops for everyone in 2024',
    description: 'Best Laptops for your budget and needs. Find the best laptop for you in 2024.',
    button: 'Read more',
    blogName: 'best-laptops-2024'

  },
  {
    image: smartBoard,
    title: 'BenQ Smart Board: The Ultimate Guide',
    description: 'Everything you need to know about BenQ Smart Board. Features, benefits, and more.',
    button: 'Read more',
    blogName: 'smart-boards-india-2024'

  },

];
</script>
