<template>
    <div class="flex flex-col md:flex-row flex-wrap gap-6 max-w-[1920px]">
      <div
        v-for="{
          image,
          title,
          subtitle,
          description,
          buttonText,
          backgroundColor,
          reverse,
          titleClass,
          subtitleClass,
          link,
        } in displayDetails"
        :key="title"
        :class="[
          'relative flex md:max-w-[1920px] md:[&:not(:first-of-type)]:flex-1 md:first-of-type:w-full',
          backgroundColor,
        ]"
      >
        <router-link
          class="absolute w-full h-full z-1 focus-visible:outline focus-visible:rounded-lg"
          :aria-label="title"
          :to="link"
        />
        <div :class="['flex justify-between overflow-hidden grow', { 'flex-row-reverse': reverse }]">
          <div class="flex flex-col justify-center items-start p-6 lg:p-10 max-w-1/2">
            <p :class="['uppercase  block font-bold tracking-widest', subtitleClass]">
              {{ subtitle }}
            </p>
            <h2 :class="['mb-4 mt-2 font-bold prose prose-xl', titleClass]">
              {{ title }}
            </h2>
            <p class=" block mb-4">
              {{ description }}
            </p>
            <SfButton class="!bg-black">{{ buttonText }}</SfButton>
          </div>
          <img :src="image" :alt="title" class="w-1/2 self-end object-cover" />
        </div>
      </div>
    </div>
  </template>
  
  import { from } from '@apollo/client';
<script lang="ts" setup>
  import { SfButton } from '@storefront-ui/vue';
 
  
  import beforeYouBuy from '@/assets/images/blog/before-your-buy.png';
  import workanywhere from '@/assets/images/work-anywhere.png';
  import smartBoard from '@/assets/images/products/benq-smart-board.png';
  import workplaceTrends from '@/assets/images/blog/workplace.png'
  
  const displayDetails = [
    {
      image: beforeYouBuy,
      title: "Projector Buying Guide 2024",
      subtitle: 'Guide',
      description: 'What Do You Need To Know before buying a project in 2024?',
      buttonText: 'Learn now',
      reverse: false,
      backgroundColor: 'bg-primary-200',
      titleClass: 'md:!text-5xl  !prose-2xl',
      subtitleClass: 'md:prose-2xl sm:prose-sm',
      descriptionClass: 'md:text-lg',
      link: "/blog/projector-buying-guide-2024",
    },
    {
      image: workanywhere,
      title: 'Best Laptops for everyone in 2024',
      subtitle: 'Guide',
      description: '2024 brings in a lot of new laptops. Here are the best ones for everyone',
      buttonText: 'Discover now',
      reverse: false,
      backgroundColor: 'bg-primary-200',
      titleClass: 'md:typography-display-2',
      subtitleClass: 'md:typography-headline-6',
      descriptionClass: 'md:text-lg',
      link: '/products',

    },
    {
      image: smartBoard,
      title: 'How much does a smart board cost in 2024?',
      subtitle: 'Blog',
      description: 'Here is how much you should plan to spend to get a touch screen TV for your classroom or meeting room.',
      buttonText: 'Discover now',
      reverse: true,
      backgroundColor: 'bg-primary-300',
      link: '/products',

    },
    
    {
      image: workplaceTrends,
      title: 'BenQ Predicts Five Key Digital Workplace Trends for 2024',
      subtitle: 'Trends',
      description: '',
      buttonText: 'Discover now',
      reverse: false,
      backgroundColor: 'bg-primary-200',
      link: '/products',

    },
    
  ];
  </script>
  