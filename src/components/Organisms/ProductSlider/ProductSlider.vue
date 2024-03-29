<template>
  <SfScrollable
    class="m-auto py-4 items-center w-full [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]"
    buttons-placement="floating"
    drag
  >
    <!-- Previous Button -->
    <template #previousButton="defaultProps">
      <SfButton
        v-bind="defaultProps"
        class="absolute !rounded-full z-10 left-4 bg-white hidden md:block"
        :class="{ '!hidden': defaultProps.disabled }"
        variant="secondary"
        size="lg"
        square
      >
        <SfIconChevronLeft />
      </SfButton>
    </template>

    <!-- Product List -->
    <div
      v-for="{ id, name, price, img } in products"
      :key="id"
      class="first:ms-auto last:me-auto border border-neutral-200 shrink-0 rounded-md hover:shadow-lg w-[148px] lg:w-[192px]"
    >
      <!-- Product Image -->
      <div class="relative">
        <SfLink href="#" class="block">
          <img
            :src="img.src"
            :alt="img.alt"
            class="block object-cover h-auto rounded-md aspect-square lg:w-[190px] lg:h-[190px]"
            width="146"
            height="146"
          />
        </SfLink>
        <SfButton
          variant="tertiary"
          size="sm"
          square
          class="absolute bottom-0 right-0 mr-2 mb-2 bg-white ring-1 ring-inset ring-neutral-200 !rounded-full"
          aria-label="Add to wishlist"
        >
          <SfIconFavorite size="sm" />
        </SfButton>
      </div>

      <!-- Product Details -->
      <div class="p-2 border-t border-neutral-200 typography-text-sm">
        <SfLink href="#" variant="secondary" class="no-underline">{{ name }}</SfLink>
        <span class="block mt-2 font-bold">{{ price }}</span>
      </div>
    </div>

    <!-- Next Button -->
    <template #nextButton="defaultProps">
      <SfButton
        v-bind="defaultProps"
        class="absolute !rounded-full z-10 right-4 bg-white hidden md:block"
        :class="{ '!hidden': defaultProps.disabled }"
        variant="secondary"
        size="lg"
        square
      >
        <SfIconChevronRight />
      </SfButton>
    </template>
  </SfScrollable>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';
import {
  SfLink,
  SfButton,
  SfIconFavorite,
  SfIconChevronLeft,
  SfIconChevronRight,
  SfScrollable,
} from '@storefront-ui/vue';

interface Product {
  id: number;
  name: string;
  price: number;
  img: { src: string; alt: string };
}

 defineProps({
  products: {
    type: Array as PropType<Product[]>,
    default: () => []
  },
});
</script>