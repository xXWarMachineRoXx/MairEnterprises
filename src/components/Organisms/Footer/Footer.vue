<template>
    <footer class="pt-10 bg-primary-300">
      <!-- <div
        class="grid justify-center grid-cols-[1fr_1fr] md:grid-cols-[repeat(4,1fr)] px-4 md:px-6 pb-10 max-w-[1536px] mx-auto md:gap-8 md:pb-6 "
      >
        <img src="/logo-inline-long.svg" alt="logo">
        

        
        <ul v-for="{ label, subcategories } in categories" :key="label" class="grid grid-cols xs:pb-4 !ml-[300px]">
          <li class="ml-4 text-lg font-medium leading-7 text-neutral-900 font-body">{{ label }}</li>
          <SfListItem
            v-for="{ subcategoryLabel, link } in subcategories"
            :key="subcategoryLabel"
            class="py-2 !bg-transparent typography-text-sm font-body"
          >
            <SfLink
              class="no-underline text-neutral-600 hover:underline hover:!text-neutral-900 active:underline active:!text-neutral-900"
              variant="secondary"
              :href="link"
            >
              {{ subcategoryLabel }}
            </SfLink>
          </SfListItem>
        </ul>
      </div> -->
      <!-- <hr /> -->
      <!-- <img class="max-w-[300px] ml-3" src="/logo-inline-long.svg" alt="logo"> -->
      <div class="py-10 md:flex md:mx-auto max-w-[1536px]">

        <div v-for="{ label, icon, link, details } in contactOptions" :key="label" class="mx-auto my-4 text-center">
          <component :is="icon" size="lg" />
          <p class="py-1 my-2 font-medium typography-text-lg font-body">
            <SfLink
              variant="secondary"
              class="no-underline text-neutral-600 hover:underline hover:!text-neutral-900 active:underline active:!text-neutral-900"
              :href="link"
            >
              {{ label }}
            </SfLink>
          </p>
          <p v-for="option in details" :key="option" class="leading-5 typography-text-sm text-neutral-600 font-body">
            {{ option }}
          </p>
        </div>
      </div>
      <div class="bg-primary-500 justify-end px-4 py-10 md:flex md:py-6  mx-auto">
        <div class="flex justify-center py-2 gap-x-4 md:self-start">
          <SfButton
            v-for="{ label, link, icon } in socialMedia"
            :key="label"
            tag="a"
            square
            variant="tertiary"
            class="text-white active:text-white hover:text-white hover:!bg-neutral-500 active:!bg-transparent"
            :href="link"
            :aria-label="`Go to ${label} page`"
          >
            <component :is="icon" />
          </SfButton>
        </div>
        <div class="flex items-center justify-center gap-6 py-2 my-4 md:ml-auto md:my-0">
          <SfLink
            v-for="{ label, link } in bottomLinks"
            :key="label"
            variant="secondary"
            class="text-white no-underline typography-text-sm active:text-white active:underline hover:text-white hover:underline"
            :href="link"
          >
            {{ label }}
          </SfLink>
        </div>
        <p
          class="flex items-center justify-center py-2 leading-5 text-center typography-text-sm text-white/50 font-body md:ml-6"
        >
          @2024 Mair Enterprises. All rights reserved.
        </p>
      </div>
    </footer>
  </template>
  <script lang="ts" setup>
  import {
    SfIconContactSupport,
    SfIconFacebook,
    SfIconHelp,
    SfIconInstagram,
    SfIconCall,
    SfIconPinterest,
    SfIconTwitter,
    SfIconYoutube,
    SfButton,
    SfLink,
    SfListItem,
  } from '@storefront-ui/vue';
  // import logo from '@/assets/logo.svg';
  const categories = [
    {
      label: 'Sitemap',
      subcategories: [
        {
          subcategoryLabel: 'Payment methods',
          link: '#',
        },
        {
          subcategoryLabel: 'Order pickup',
          link: '#',
        },
        {
          subcategoryLabel: 'Purchase status',
          link: '#',
        },
        {
          subcategoryLabel: 'Track orders',
          link: '#',
        },
        {
          subcategoryLabel: 'Returns',
          link: '#',
        },
      ],
      
    },
    
    {
      label: 'Sitemap',
      subcategories: [
        {
          subcategoryLabel: 'Payment methods',
          link: '#',
        },
        {
          subcategoryLabel: 'Order pickup',
          link: '#',
        },
        {
          subcategoryLabel: 'Purchase status',
          link: '#',
        },
        {
          subcategoryLabel: 'Track orders',
          link: '#',
        },
        {
          subcategoryLabel: 'Returns',
          link: '#',
        },
      ],
      
    },

  ];
  const socialMedia = [
    {
      label: 'Facebook',
      link: '#',
      icon: SfIconFacebook,
    },
    {
      label: 'Twitter',
      link: '#',
      icon: SfIconTwitter,
    },
    {
      label: 'Instagram',
      link: '#',
      icon: SfIconInstagram,
    },
    {
      label: 'Pinterest',
      link: '#',
      icon: SfIconPinterest,
    },
    {
      label: 'Youtube',
      link: '#',
      icon: SfIconYoutube,
    },
  ];
  const contactOptions = [
    {
      label: 'Help center (coming soon)',
      link: '#',
      details: ['Find answers online anytime'],
      icon: SfIconHelp,
    },
    {
      label: 'Live chat (coming soon)',
      link: '#',
      details: ['Mon–Fri, 5am–10pm IST', 'Sat–Sun, 6am–9pm IST'],
      icon: SfIconContactSupport,
    },
    {
      label: '+91 794 296 9133',
      link: 'tel:+917942969133',
      details: ['Mon–Fri, 5am–10pm IST', 'Sat–Sun, 6am–9pm IST'],
      icon: SfIconCall,
    },
  ];
  const bottomLinks = [
    {
      label: 'Terms',
      link: '#',
    },
    {
      label: 'Privacy policy',
      link: '#',
    },
  ];
  </script>
  