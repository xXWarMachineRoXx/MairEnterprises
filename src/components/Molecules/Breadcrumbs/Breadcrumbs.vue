<template>
  <nav class="inline-flex items-center text-sm font-normal font-body">
    <ol class="flex w-auto leading-none group md:flex-wrap">
      <li class="flex items-center sm:hidden text-neutral-500">
        <SfDropdown v-model="dropdownOpened" strategy="absolute" placement="bottom-start" @update:model-value="close">
          <template #trigger>
            <SfButton
              class="relative w-5 h-5 !p-0 rounded-sm outline-secondary-600 hover:bg-transparent active:bg-transparent"
              aria-label="More breadcrumbs" variant="tertiary" square @click="toggle">
              <template #prefix>
                <SfIconMoreHoriz size="sm"
                  class="text-neutral-500 hover:text-primary-700 active:text-primary-800 active:bg-transparent" />
              </template>
            </SfButton>
          </template>
          <div class="px-4 py-2 rounded-md shadow-md border-neutral-100">
      <li v-for="item in dynamicBreadcrumbs" :key="item.name" class="py-2 last-of-type:hidden">
        <router-link :to="item.link" class="leading-5 no-underline text-inherit hover:underline active:underline whitespace-nowrap outline-secondary-600">
          {{ item.name }}
        </router-link>
        <!-- <SfLink :href="item.link" variant="secondary"
          class="leading-5 no-underline text-inherit hover:underline active:underline whitespace-nowrap outline-secondary-600">
          {{ item.name }}
        </SfLink> -->
      </li>
      </div>
      </SfDropdown>
      </li>
      <li v-for="(item, index) in dynamicBreadcrumbs" :key="item.name"
        class="peer hidden sm:flex items-center peer-[:nth-of-type(even)]:before:content-['/'] peer-[:nth-of-type(even)]:before:px-2 peer-[:nth-of-type(even)]:before:leading-5 last-of-type:flex last-of-type:before:font-normal last-of-type:before:text-neutral-500 text-neutral-500 last-of-type:text-neutral-900 last-of-type:font-medium">
        <!-- <SfLink v-if="index === 0" :href="item.link" variant="secondary"
          class="inline-flex leading-5 no-underline hover:underline active:underline whitespace-nowrap outline-secondary-600 text-neutral-500">
          <SfIconHome size="sm" />
        </SfLink> -->
        <router-link v-if="index === 0" :to="item.link" variant="secondary"
          class="inline-flex leading-5 no-underline hover:underline active:underline whitespace-nowrap outline-secondary-600 text-neutral-500">
          <SfIconHome size="sm" />
        </router-link>
        <router-link v-else-if="index < dynamicBreadcrumbs.length - 1" :to="item.link" variant="secondary"
          class="leading-5 no-underline hover:underline active:underline whitespace-nowrap outline-secondary-600 text-inherit">
          {{ item.name }}
        </router-link>
        <!-- <SfLink v-else-if="index < dynamicBreadcrumbs.length - 1" :href="item.link" variant="secondary"
          class="leading-5 no-underline hover:underline active:underline whitespace-nowrap outline-secondary-600 text-inherit">
          {{ item.name }}
        </SfLink> -->
        <span v-else>
          {{ item.name }}
        </span>
      </li>
    </ol>
  </nav>
</template>
  
<script lang="ts" setup>
// import { SfDropdown, SfButton, SfLink, SfIconMoreHoriz, SfIconHome } from '@storefront-ui/vue';
import { SfDropdown, SfButton, SfIconMoreHoriz, SfIconHome } from '@storefront-ui/vue';

import { ref,computed } from 'vue';
import { useRoute } from 'vue-router';

// const breadcrumbs = [
//   {
//     name: 'Home',
//     link: '#',
//   },
//   { name: 'Page 2', link: '#' },
//   { name: 'Page 3', link: '#' },
//   { name: 'Page 4', link: '#' },
//   { name: 'Page 5', link: '#' },
// ];

const dropdownOpened = ref(false);
const close = () => {
  dropdownOpened.value = false;
};
const toggle = () => {
  dropdownOpened.value = !dropdownOpened.value;
};
const route = useRoute();
// Example static part of the breadcrumbs
const staticBreadcrumbs = [
  { name: 'Home', link: '/' },
];
const dynamicBreadcrumbs = computed(() => {
  // Generate dynamic breadcrumbs based on the current route
  // This is a simple example; you should adjust it according to your routing logic
  let dynamicParts = route.path.split('/').filter(part => part);
  return [
    ...staticBreadcrumbs,
    ...dynamicParts.map((part, index) => {
      return {
        name: part.charAt(0).toUpperCase() + part.slice(1), // Capitalize the first letter
        link: '/' + dynamicParts.slice(0, index + 1).join('/')
      };
    })
  ];
});
</script>
  