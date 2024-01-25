<template>
  <div class="border border-neutral-200 rounded-md hover:shadow-lg max-w-[300px]">
    <div class="relative">
      <!-- <router-link :to=productRoute>
        <SfLink class="block">
          <img :src=img :alt=alt class="block object-cover h-auto rounded-md aspect-square" width="300" height="300" />
        </SfLink>
      </router-link> -->
      <router-link :to=productRoute>
        
          <img :src=img :alt=alt class="block object-cover h-auto rounded-md aspect-square" width="300" height="300" />
        
      </router-link>
      <SfChip class="absolute top-0 left-0 mt-2 ml-2" :class="{
        'bg-primary-500': category === 'New',
        'bg-secondary-500 text-orange-50': category === 'Sale',
        'bg-primary-100 !text-secondary-900': category === 'Top Rated',
        'bg-primary-200 !text-secondary-900': category === 'Projectors',

      }" v-if="category">
        {{ category }}
      </SfChip>
      <SfButton v-if="canWishlist" variant="tertiary" size="sm" square
        class="absolute bottom-0 right-0 mr-2 mb-2 bg-white ring-1 ring-inset ring-neutral-200 !rounded-full"
        aria-label="Add to wishlist">
        <SfIconFavorite size="sm" />
      </SfButton>

    </div>
    <div class="p-4 border-t border-neutral-200">
      <router-link :to=productRoute>
        <SfLink :href=productRoute variant="secondary" class="no-underline"> {{ productName }} </SfLink>
      </router-link>
      
      <div class="flex items-center pt-1">
        <SfRating size="xs" :value=averageRating :max="5" half-increment />


        <SfLink href="#" variant="secondary" class="pl-1 no-underline">
          <SfCounter size="xs">{{ numberofReviews }}1</SfCounter>
        </SfLink>
      </div>
      <p class="block py-2 font-normal leading-5 typography-text-sm text-neutral-700">
        {{ description }}
      </p>
      <span class="block pb-2 font-bold typography-text-lg">₹ {{ price }}</span>

      <SfButton @click="call" size="sm">
        <template #prefix>
          <SfIconHelp size="sm" />
        </template>
        Interested
      </SfButton>
      <SfButton @click="$router.push('/products/'+productLink);console.log(numberofReviews)" size="sm" variant="secondary" class="ml-1">
        <template #prefix>
          <SfIconInfo size="sm" />
        </template>
        More Info
      </SfButton>
    </div>
  </div>
</template>
  
<script lang="ts" setup>
import { computed } from 'vue';
import { SfRating, SfChip, SfCounter, SfLink, SfButton, SfIconHelp, SfIconFavorite, SfIconInfo } from '@storefront-ui/vue';
// Create a computed property to generate the correct route for the product

const props = defineProps({
  img: String,
  alt: String,
  productName: String,
  price: String,
  category: String,
  description: String,
  numberofReviews: Number,
  averageRating: Number,
  canWishlist: Boolean,
  productLink: String,
});
const productRoute = computed(() => `/products/${props.productLink}`);
const call = () => {
  location.href = "tel:+917942969133";
};
</script>
  