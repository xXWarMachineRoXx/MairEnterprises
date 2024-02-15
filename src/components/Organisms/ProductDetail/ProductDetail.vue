<template>
  <section class="md:max-w-[640px]">
    <div class="inline-flex items-center justify-center text-sm font-medium text-white bg-secondary-600 py-1.5 px-3 mb-4">
      <SfIconSell size="sm" class="mr-1.5" />
      Sale
    </div>
    <h1 class="mb-1  typography-headline-4">{{ productName }}</h1>
    <strong class="block font-bold text-3xl">₹{{ price }}</strong>
    <div class="inline-flex items-center mt-4 mb-2">
      <SfRating size="xs" :value="rating" :max="5" />
      <SfCounter class="ml-1" size="xs">{{ numberofReviews }}</SfCounter>
      <SfLink href="#" variant="secondary" class="ml-2 text-xs text-neutral-500"> {{ numberofReviews }} reviews </SfLink>
    </div>
    <ul class="mb-4 font-normal typography-text-sm">
      <li v-for="line in productDescription">
        ● {{ line }}
      </li>
    </ul>
  
    <div class="flex items-center gap-2 mb-4">
      <SfIconShoppingCart size="sm" class="flex-shrink-0 text-neutral-500" />
      <p class="text-sm text-neutral-500">Your current total : ₹{{ priceInt*count.valueOf() }}</p>
    </div>
    <div class="py-4 mb-4 border-gray-200 border-y">
      <!-- <div
        class="bg-primary-100 text-primary-700 flex justify-center gap-1.5 py-1.5 typography-text-sm items-center mb-4 rounded-md">
        <SfIconShoppingCartCheckout />
        1 in cart
      </div> -->
      <div class="items-start xs:flex">
        <div class="flex flex-col items-stretch xs:items-center xs:inline-flex">
          <div class="flex border border-neutral-300 rounded-md">
            <SfButton variant="tertiary" :disabled="count <= min" square class="rounded-r-none p-3"
              :aria-controls="inputId" aria-label="Decrease value" @click="dec()">
              <SfIconRemove />
            </SfButton>
            <input :id="inputId" v-model="count" type="number"
              class="grow appearance-none mx-2 w-8 text-center bg-transparent font-medium [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-inner-spin-button]:display-none [&::-webkit-inner-spin-button]:m-0 [&::-webkit-outer-spin-button]:display-none [&::-webkit-outer-spin-button]:m-0 [-moz-appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none disabled:placeholder-disabled-900 focus-visible:outline focus-visible:outline-offset focus-visible:rounded-sm"
              :min="min" :max="max" @input="handleOnChange" />
            <SfButton variant="tertiary" :disabled="count >= max" square class="rounded-l-none p-3"
              :aria-controls="inputId" aria-label="Increase value" @click="inc()">
              <SfIconAdd />
            </SfButton>
          </div>
          <p class="self-center mt-1 mb-4 text-xs text-neutral-500 xs:mb-0">
            <strong class="text-neutral-900">{{ max }}</strong> in stock
          </p>
        </div>
        <SfButton @click="call" size="lg" class="w-full xs:ml-4">
          <template #prefix>
            <SfIconCall size="sm" />
          </template>
          Inquire now
        </SfButton>
      </div>
      <div class="flex justify-center mt-4 gap-x-4">
        <!-- <SfButton size="sm" variant="tertiary">
          <template #prefix>
            <SfIconCompareArrows size="sm" />
          </template>
          Compare
        </SfButton>
        <SfButton size="sm" variant="tertiary">
          <SfIconFavorite size="sm" />
          Add to list
        </SfButton> -->
      </div>
    </div>
    <div class="flex first:mt-4">
      <SfIconPackage size="sm" class="flex-shrink-0 mr-1 text-neutral-500" />
      <p class="text-sm">
        Minimum order quantity: 5, Available to buy by call only.
        <!-- <SfLink href="#" variant="secondary" class="mx-1"> Add an address </SfLink>
        to see options -->
        <!-- <SfLink href="#" variant="secondary" class="mx-1"> Add an address </SfLink> -->

      </p>
    </div>
    <!-- <div class="flex mt-4">
      <SfIconWarehouse size="sm" class="flex-shrink-0 mr-1 text-neutral-500" />
      <p class="text-sm">
        Pickup not available at your shop.
        <SfLink href="#" variant="secondary" class="ml-1"> Check availability nearby </SfLink>
      </p>
    </div> -->
    <div class="flex mt-4">
      <SfIconCall size="sm" class="flex-shrink-0 mr-1 text-neutral-500" />
      <p class="text-sm">
        Call for any queries at
        <SfLink href="tel:+919810159599" variant="secondary" class="ml-1"> +91 9810159599 </SfLink>
      </p>
    </div>
    <div class="flex mt-4">
      <SfIconSafetyCheck size="sm" class="flex-shrink-0 mr-1 text-neutral-500" />
      <p class="text-sm">
        Return Policy is as negotiated.
        <SfLink href="#" variant="secondary" class="ml-1"> Details </SfLink>
      </p>
    </div>
    <h2 v-if="Object.keys(techspecs).length > 0" class="mb-2 font-bold typography-headline-5 mt-5">Technical specifications</h2>
    <p v-else class="mb-2 text-gray-400 prose-xs mt-5">Technical specifications not specified</p>

    <table class="border-collapse table-auto w-full border border-gray-200 mb-5">
      <tr v-for="(value, key) in techspecs" :key="key" class="border-b border-gray-200">
        <td class="py-2 px-4 text-sm text-gray-500">{{ key }}</td>
        <td class="py-2 px-4 text-sm text-gray-900">{{ value }}</td>
      </tr>
      
      <!-- Add more rows as needed -->
    </table>
  </section>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue';
// import {
//   SfButton,
//   SfCounter,
//   SfLink,
//   SfRating,
//   SfIconSafetyCheck,
//   SfIconCompareArrows,
//   SfIconWarehouse,
//   SfIconPackage,
//   SfIconFavorite,
//   SfIconSell,
//   SfIconShoppingCart,
//   SfIconAdd,
//   SfIconRemove,
//   useId,
//   SfIconCall,
// } from '@storefront-ui/vue';
import {
  SfButton,
  SfCounter,
  SfLink,
  SfRating,
  SfIconSafetyCheck,
  SfIconPackage,
  SfIconSell,
  SfIconShoppingCart,
  SfIconAdd,
  SfIconRemove,
  useId,
  SfIconCall,
} from '@storefront-ui/vue';
import { clamp } from '@storefront-ui/shared';
import { useCounter } from '@vueuse/core';


function call() {
  location.href = "tel:+919810159599";
}
const inputId = useId();
const min = ref(1);
const max = ref(295);
const { count, inc, dec, set } = useCounter(1, { min: min.value, max: max.value });
function handleOnChange(event: Event) {
  const currentValue = (event.target as HTMLInputElement)?.value;
  const nextValue = parseFloat(currentValue);
  set(clamp(nextValue, min.value, max.value));
}
// const total=count*priceInt;
// const total=ref(count.value*priceInt);
// console.log("count", count.value);
defineProps({
  productName: {
    type: String || Array<String> || Object || Array<Object>,
    required: true,
  },
  productDescription: {
    type: [String, Array, Object],
    required: true,
  },
  techspecs: {
    type: Object,
    required: true,
  },
  price: {
    type: [String, Number],
    required: true,
  },
  priceInt: {
    type: Number,
    required: true,
  },
  rating: {
    type: Number,
    required: true,
  },
  numberofReviews: {
    type: Number,
    required: true,
  }
});
</script>
  