<template>
  <div class="relative flex w-full max-h-[600px] aspect-[4/3]">
    <a></a>
    <router-link to="/product/1">
      <div class="w-full h-full">
        <img :src="img" :alt="alt" class="object-cover w-auto h-full" />
        hello
      </div>
    </router-link>
    <SfScrollable
      class="w-full h-full snap-x snap-mandatory [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]"
      :active-index="activeIndex" direction="vertical" wrapper-class="h-full m-auto" is-active-index-centered
      buttons-placement="none" :drag="{ containerWidth: true }" @on-drag-end="onDragged">
      <div class="relative flex w-full max-h-[600px] aspect-[4/3]">
        <div class="w-full h-full">
          <img :src="img" :alt="alt" class="object-cover w-auto h-full" />
        </div>
      </div>
    </SfScrollable>
  </div>
</template>
  
<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import {
  SfScrollable,
  type SfScrollableOnDragEndData,
} from '@storefront-ui/vue';
import { unrefElement, useIntersectionObserver } from '@vueuse/core';
// import { watch, type ComponentPublicInstance } from 'vue';
import { watch } from 'vue';

import benq from '@/assets/images/benq.png';
const props = defineProps({
  img: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    required: true,
  },
});

onMounted(() => {
  console.log(props.img)
})
// const withBase = (filepath: string) => `/src/assets/images/products/${filepath}`;
const images = [
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq1' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq2' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq3' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq4' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq5' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq6' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq7' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq8' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq9' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq10' },
  { imageSrc: benq, imageThumbSrc: benq, alt: 'benq11' },
];

const thumbsRef = ref<HTMLElement>();
const firstThumbRef = ref<HTMLButtonElement>();
const lastThumbRef = ref<HTMLButtonElement>();
const firstThumbVisible = ref(false);
const lastThumbVisible = ref(false);
const activeIndex = ref(0);

watch(
  thumbsRef,
  (thumbsRef) => {
    if (thumbsRef) {
      useIntersectionObserver(
        firstThumbRef,
        ([{ isIntersecting }]) => {
          firstThumbVisible.value = isIntersecting;
        },
        {
          root: unrefElement(thumbsRef),
          rootMargin: '0px',
          threshold: 1,
        },
      );
    }
  },
  { immediate: true },
);

watch(
  thumbsRef,
  (thumbsRef) => {
    if (thumbsRef) {
      useIntersectionObserver(
        lastThumbRef,
        ([{ isIntersecting }]) => {
          lastThumbVisible.value = isIntersecting;
        },
        {
          root: unrefElement(thumbsRef),
          rootMargin: '0px',
          threshold: 1,
        },
      );
    }
  },
  { immediate: true },
);

const onDragged = (event: SfScrollableOnDragEndData) => {
  if (event.swipeRight && activeIndex.value > 0) {
    activeIndex.value -= 1;
  } else if (event.swipeLeft && activeIndex.value < images.length - 1) {
    activeIndex.value += 1;
  }
};

// const assignRef = (el: Element | ComponentPublicInstance | null, index: number) => {
//   if (!el) return;
//   if (index === images.length - 1) {
//     lastThumbRef.value = el as HTMLButtonElement;
//   } else if (index === 0) {
//     firstThumbRef.value = el as HTMLButtonElement;
//   }
// };
</script>
  