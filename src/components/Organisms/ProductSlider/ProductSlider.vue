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
      v-for="{ id, name, price,  } in products"
      :key="id"
      class="first:ms-auto last:me-auto border border-neutral-200 shrink-0 rounded-md hover:shadow-lg w-[148px] lg:w-[192px]"
    >
      <!-- Product Image -->
      <div class="relative">
        <SfLink href="#" class="block">
          <!-- <img
            src="img.src"
            alt="img.alt"
            class="block object-cover h-auto rounded-md aspect-square lg:w-[190px] lg:h-[190px]"
            width="146"
            height="146"
          /> -->
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
import { onMounted,ref, watchEffect } from 'vue'; // Import watchEffect from 'vue' here
import { useQuery } from '@vue/apollo-composable'; // Import useQuery
import { gql } from '@apollo/client/core';
import {
  SfLink,
  SfButton,
  SfIconFavorite,
  SfIconChevronLeft,
  SfIconChevronRight,
  SfScrollable,
} from '@storefront-ui/vue';


var products = ref([]); // Define a ref for products
// Define your GraphQL query
const GET_PRODUCTS = gql`
  query{
    products {
      items {
        name
        assets {
          preview 
        }
        variants {
          priceWithTax
        }
      }
    }
  }
`;

// Use useQuery to fetch data
const { result, loading, error } = useQuery(GET_PRODUCTS);
console.log('Loading:', loading.value);
console.log('result:', result.value);
// products=result.value.products?.items;

// Watch for changes in the result and update the products ref
watchEffect(() => {
  if (!loading.value && result.value) {
    // Check for errors
    if (error.value) {
      console.error('GraphQL Error:', error.value);
      return;
    }
    const items = result.data.products.items.map((item) => {
      return {
        id: item.productId, // Assuming you have a unique identifier like productId
        name: item.name,
        price: item.variants[0]?.priceWithTax || 0, // Extract priceWithTax
        img: item.assets[0]?.preview || '', // Extract the image preview URL
      };
    });
    // Update the products ref with the fetched data
    products.value = result.value.products?.items || [];
  }
});

// Output the products in the console when they are available
onMounted(() => {
  console.log('Products:', products.value);
  console.log('Loading:', loading.value);
  console.error('GraphQL Error:', error.value);
});
</script>