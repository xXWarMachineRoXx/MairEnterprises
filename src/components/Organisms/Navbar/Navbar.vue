<template>
  <header class="flex justify-center w-full py-2 px-4 lg:py-5 lg:px-6 !bg-primary-50 border-b border-neutral-200">
    <div
      class="flex flex-wrap justify-between lg:flex-nowrap items-center flex-row md:justify-start h-full max-w-[1536px] w-full">
      <SfButton variant="tertiary" square class="md:hidden xs:invisible" aria-label="Menu">
        <SfIconMenu />
      </SfButton>
      <router-link to="/" aria-label="mair enterprises home page"
        class="inline-block mr-4 focus-visible:outline focus-visible:outline-offset focus-visible:rounded-sm shrink-0">
        <img src="/logo-inline-long.svg" alt="Sf Logo" class="w-[200px] md:h-10 md:w-[302px] lg:w-[18rem] lg:h-[2.5rem]">

      </router-link>

      <SfButton variant="tertiary" class="md:hidden float-end" square aria-label="Search" @click="open">
        <SfIconSearch />

        <!-- <SearchModal :isOpen="modalOpen" :open="openModal"  class="!z-20" /> -->
      </SfButton>
      <SearchModal :is-open="isOpen" @update:is-open="updateIsOpen" />
      <SfButton aria-label="Open categories" class="hidden md:block lg:hidden order-first lg:order-1 mr-4" square
        variant="tertiary">
        <SfIconMenu />

      </SfButton>
      <router-link to="/products">
        <SfButton class="hidden lg:flex lg:mr-4 hover:!text-primary-500" variant="tertiary">
          <template #suffix>
            <SfIconGridView class="hidden lg:block" />
          </template>
          <span class="hidden lg:flex whitespace-nowrap ">Browse products</span>
        </SfButton>
      </router-link>

      <Search class="!hidden md:!flex " />
      <nav class="flex-1 hidden md:flex justify-end lg:order-last lg:ml-4">
        <div class="flex flex-row flex-nowrap">
        
          

          <SfButton @click="$router.push(actionItem.link)" v-for="actionItem in actionItems" :key="actionItem.ariaLabel"
            class="mr-2 -ml-0.5 rounded-md text-primary-500 hover:bg-primary-100 active:bg-primary-200 hover:!text-primary-600 active:text-primary-700"
            :aria-label="actionItem.ariaLabel" variant="tertiary" square>
            <template #prefix>
              <Component :is="actionItem.icon" />
            </template>

            <span class="hidden xl:inline-flex whitespace-nowrap">{{
              actionItem.label
            }}</span>
          </SfButton>
        </div>
      </nav>
    </div>
  </header>
</template>
<script lang="ts" setup>

import { useDisclosure } from '@storefront-ui/vue';
import SearchModal from "../../../components/Molecules/SearchModal/SearchModal.vue"
import Search from '../../Molecules/Search/Search.vue';
import {
  SfButton,
  SfIconInfo,
  SfIconCall,
  SfIconViewList,
  SfIconGridView,

  SfIconSearch,
  SfIconMenu,

} from '@storefront-ui/vue';
import { RouterLink } from 'vue-router';

const actionItems = [
  {
    label: 'About Us',
    link: '/about',
    icon: SfIconInfo,
    ariaLabel: 'about us',
    role: 'about',
  },

  {
    label: 'Contact Us',
    link: '/contact',
    icon: SfIconCall,
    ariaLabel: 'Log in',
    role: 'contact',
  },
  {
    label: 'Blog',
    icon: SfIconViewList,
    link: '/blog',
    ariaLabel: 'Log in',
    role: 'blog',
  },
];

const { isOpen, open, close } = useDisclosure({ initialValue: false });




const updateIsOpen = (newIsOpen: Boolean) => {
  if (newIsOpen) {
    open();
  } else {
    close();
  }
};
</script>
  