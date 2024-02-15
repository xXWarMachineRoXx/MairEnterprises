<template>
  <form ref="referenceRef" role="search" class="relative" @submit.prevent="submit">
    <SfInput ref="inputRef" v-model="inputModel" aria-label="Search" placeholder="Search 'BenQ' or 'EPSON'..."
      @focus="open" @keydown="handleInputKeyDown" class="lg:w-[500px]  md:w-[300px] h-10 pr-0 rounded-md ">
      <template #prefix>
        <SfIconSearch />
      </template>
      <template #suffix>
        <button v-if="inputModel" type="button" aria-label="Reset search"
          class="flex rounded-md focus-visible:outline focus-visible:outline-offset" @click="reset">
          <SfIconCancel />
        </button></template>
    </SfInput>
    <div v-if="isOpen" ref="floatingRef" :style="style" class="left-0 right-0 z-10">
      <div v-if="isLoadingSnippets"
        class="flex items-center justify-center w-full h-20 py-2 bg-white border border-solid rounded-md border-neutral-100 drop-shadow-md">
        <SfLoaderCircular />
      </div>
      <ul v-else-if="snippets.length > 0" ref="dropdownListRef"
        class="py-2 bg-white border border-solid rounded-md border-neutral-100 drop-shadow-md ">
        <li v-for="{ highlight, rest, product } in snippets" :key="product.id">
          <SfListItem tag="button" type="button" class="flex justify-start items-center"
            @click="() => selectValue(Number(product.id))"
            @keydown.enter.space.prevent="selectValue(Number(product.name))">
            <img :src="product.img" :alt="product.name" class="w-8 h-8 mr-2" />
            <!-- Added 'mr-2' class for right margin -->
            <p class="text-left">
              <span class="font-bold">{{ highlight }}</span>
              <span class="font-medium">{{ rest }}</span>
            </p>
          </SfListItem>
        </li>

      </ul>
      <ul v-else-if="snippets.length == 0 && inputModel.length > 0">
        <li class="py-2 bg-white border border-solid rounded-md border-neutral-100 drop-shadow-md">
          <SfListItem class="flex justify-start">
            <p class="text-left"> No results found 🤔</p>
          </SfListItem>
        </li>
        <!-- <li class="py-2 bg-white border border-solid rounded-md border-neutral-100 drop-shadow-md">
            <SfListItem class="flex justify-start">
              <p class="text-left">Try searching for 'BenQ' or 'EPSON'</p>
            </SfListItem>
          </li> -->
      </ul>
    </div>
  </form>
</template>
  
<script lang="ts" setup>
import { type Ref, ref, watch } from 'vue';
import { offset } from '@floating-ui/vue';
import { watchDebounced } from '@vueuse/shared';
import { unrefElement } from '@vueuse/core';
import {
  SfIconCancel,
  SfIconSearch,
  SfInput,
  SfListItem,
  SfLoaderCircular,
  useDisclosure,
  useDropdown,
  useTrapFocus,
} from '@storefront-ui/vue';

import router from '../../../router';
import { useProductsStore } from '../../../stores/productStore'; // Adjust the path as per your project structure

// Define the store instance
const productsStore = useProductsStore();
const products = productsStore.products
const inputModel = ref('');
const inputRef = ref();
const dropdownListRef = ref();
const isLoadingSnippets = ref(false);
const snippets = ref<{ highlight: string; rest: string; product: Product, link: string,img: string }[]>([]);
const { isOpen, close, open } = useDisclosure();
const { referenceRef, floatingRef, style } = useDropdown({
  isOpen,
  onClose: close,
  placement: 'bottom-start',
  middleware: [offset(4)],
});
const { focusables: focusableElements } = useTrapFocus(dropdownListRef as Ref<HTMLElement>, {
  trapTabs: false,
  arrowKeysUpDown: true,
  activeState: isOpen,
  initialFocus: false,
});

const submit = () => {
  close();
  alert(`Search for phrase: ${inputModel.value}`);
};

const focusInput = () => {
  const inputEl = unrefElement(inputRef)?.querySelector('input');
  inputEl?.focus();
};

const reset = () => {
  inputModel.value = '';
  snippets.value = [];
  close();
  focusInput();
};

// Update this function to route to the selected product
const selectValue = (productId: number) => {
  // Retrieve the product details based on the ID from your Pinia store
  const selectedProduct = productsStore.products.find(product => product.id === productId);
  if (selectedProduct) {
    // Route to the selected product
    router.push(`/products/${selectedProduct.productLink}`);
    close();
    focusInput();
  }
};
const handleInputKeyDown = (event: KeyboardEvent) => {
  if (event.key === 'Escape') reset();
  if (event.key === 'ArrowUp') {
    open();
    if (isOpen && focusableElements.value.length > 0) {
      focusableElements.value[focusableElements.value.length - 1].focus();
    }
  }
  if (event.key === 'ArrowDown') {
    open();
    if (isOpen && focusableElements.value.length > 0) {
      focusableElements.value[0].focus();
    }
  }
};

watch(inputModel, () => {
  if (inputModel.value === '') {
    reset();
  }
});

watchDebounced(
  inputModel,
  () => {
    if (inputModel.value) {
      const getSnippets = async () => {
        open();
        isLoadingSnippets.value = true;
        try {
          const data = await mockAutocompleteRequest(inputModel.value);
          snippets.value = data as unknown as { highlight: string; rest: string; product: { id: string; name: string; link: string; img: string }; link: string; img: string }[];
        } catch (error) {
          close();
          console.error(error);
        }
        isLoadingSnippets.value = false;
      };

      getSnippets();
    }
  },
  { debounce: 500 },
);

interface Product {
  id: string;
  name: string;
  img: string;
}
const mockProducts = products.map(item => ({
  id: item.id,
  name: item.productName,
  link: item.productLink,
  img: item.img
}));

// Just for presentation purposes. Replace mock request with the actual API call.
const delay = () => new Promise((resolve) => setTimeout(resolve, Math.random() * 1000));
const mockAutocompleteRequest = async (phrase: string) => {
  await delay();
  const results = mockProducts
    .filter((product) => product.name.toLowerCase().startsWith(phrase.toLowerCase()))
    .map((product) => {
      const highlight = product.name.substring(0, phrase.length);
      const rest = product.name.substring(phrase.length);
      return { highlight, rest, product };
    });
  return results;
};
</script>
  