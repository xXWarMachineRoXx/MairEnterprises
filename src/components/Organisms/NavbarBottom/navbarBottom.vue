<template>
    <nav class="max-w-[700px] !bottom-0 w-full left-0 fixed flex flex-row items-stretch z-10">
      <SfButton
        v-for="item in items"
        :key="item.label"
        variant="tertiary"
        :class="[
          'py-1 flex flex-col h-full w-full rounded-none bg-primary-700 text-white hover:text-white hover:bg-primary-800 active:text-white active:bg-primary-900',
          { 'text-white bg-primary-900': selectedItem === item.label },
        ]"
        @click="onClickHandler(item.label);$router.push(item.link)"
      >
        <template #prefix>
          <Component :is="item.icon" />
        </template>
        {{ item.label }}
      </SfButton>
    </nav>
  </template>
  <script setup lang="ts">
  import { ref } from 'vue';
  import { SfButton, SfIconHome, SfIconGridView, SfIconViewList, SfIconInfo, SfIconCall } from '@storefront-ui/vue';

  
  const items = [
    {
      label: 'Home',
      icon: SfIconHome,
      link: '/',
    },
    {
      label: 'Blog',
      icon: SfIconViewList,
      link: '/blog',
    },
    {
      label: 'Products',
      icon: SfIconGridView,
      link: '/products',
    },
    {
      label: 'About',
      icon: SfIconInfo,
      link: '/about',
    },
    {
      label: 'Contact',
      icon: SfIconCall,
      link: '/contact',
    },
  ];
  const selectedItem = ref('');
  function onClickHandler(itemLabel: string) {
    selectedItem.value = itemLabel;
  }
  </script>
  