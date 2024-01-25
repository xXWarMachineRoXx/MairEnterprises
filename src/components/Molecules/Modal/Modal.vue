<template>
  <!-- Backdrop -->
  <transition enter-active-class="transition duration-200 ease-out" leave-active-class="transition duration-200 ease-out"
    enter-from-class="opacity-0" enter-to-class="opacity-100" leave-from-class="opacity-100" leave-to-class="opacity-0">
    <div v-if="props.isOpen" class="fixed inset-0 bg-neutral-700 bg-opacity-50 z-50" @click="closeModal" />
  </transition>

  <!-- Modal -->
  <transition enter-active-class="transition duration-200 ease-out" leave-active-class="transition duration-200 ease-out"
    enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0"
    leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
    <div v-if="props.isOpen" class="fixed inset-0 flex items-center justify-center z-50" role="alertdialog"
      aria-labelledby="promoModalTitle" aria-describedby="promoModalDesc">
      <div class="max-w-[90%] md:max-w-lg bg-white p-4 rounded-lg">
        <header>
          <SfButton square variant="tertiary" class="absolute right-2 top-2" @click="closeModal">
            <SfIconClose />
          </SfButton>
          <h3 id="promoModalTitle" class="font-bold typography-headline-4 md:typography-headline-3">
            Search for products
          </h3>
        </header>
        <div class="mt-4">
          <SearchVue />
        </div>
        <footer class="flex justify-end gap-4 mt-4">
          <SfButton variant="secondary" @click="closeModal">Skip</SfButton>
          <SfButton @click="closeModal">Yes!</SfButton>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { SfModal, SfButton, SfIconClose } from '@storefront-ui/vue';
import SearchVue from '../Search/Search.vue';

const props = defineProps({
  isOpen: Boolean
});

const emit = defineEmits(['update:isOpen']);

const closeModal = () => {
  emit('update:isOpen', false);
};
</script>
