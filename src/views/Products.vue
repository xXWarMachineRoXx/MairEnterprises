<template class="!bg-primary-500">
  <Navbar />
  <NavbarBottom class="md:hidden lg:hidden sm:hidden"/>
  <div class="mx-14 my-8 p-4">
    <Breadcrumbs />
    <h1 class="font-bold text-4xl"> Browse Products </h1>
    <div class="flex lg:gap-20 md:gap-8 sm:gap-1">
      <FilterSideBar />
      <div class="flex flex-col gap-8">
        <!-- <p class="text-lg font-bold text-center"></p> -->
        <p v-if="Object.values(productsStore.filterCriteria)[0]===''" class="text-lg font-bold  "> All products <SfCounter>{{ products.length }}</SfCounter></p>
        <p v-if="Object.values(productsStore.filterCriteria)[0]!==''" class="text-lg font-bold  "> Showing <SfCounter>{{ products.length }}</SfCounter> <SfChip class="ml-3">{{ Object.values(productsStore.filterCriteria)[0] }}</SfChip></p>
        
        <!-- <template>
            <ul class="flex flex-wrap gap-4 sm:flex-row">
              <li v-for="(item, index) in chipValues" :key="item.value">
                <SfChip v-model="selectedValues" :input-props="{ value: item.value }"
                  @update:model-value="handleChipRemove(index)">
                  <template #prefix>
                    <SfThumbnail :class="`bg-${item.value}-500`" />
                  </template>
                  {{ item.label }}
                  <template #suffix>
                    <SfIconCloseSm
                      class="text-neutral-500 hover:text-primary-800 active:text-primary-900 disabled:opacity-20" />
                  </template>
                </SfChip>
              </li>
            </ul>
          </template> -->

        <div v-if="products.length === 0 || Object.keys(productsStore.filteredProducts).length < 1"
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4  gap-4">
          <ProductCard v-for="product in products" :key="product.id" :img="product.img" :alt="product.alt"
            :productName="product.productName"  :description="product.description"
            :numberofReviews="product.numberofReviews" :category="product.category" :canWishlist="product.canWishlist"
            :averageRating="product.averageRating" :productLink="product.productLink" />
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          

          <ProductCard v-for="product in products" :key="product.id" :img="product.img" :alt="product.alt"
            :productName="product.productName"  :description="product.description"
            :numberofReviews="product.numberofReviews" :category="product.category" :canWishlist="product.canWishlist"
            :averageRating="product.averageRating" :productLink="product.productLink" />
        </div>

      </div>
      
    </div>
    
    
  </div>
  <TrustBanner class="mt-20" />
    <Footer />
</template>

<script lang="ts">
import { ref, defineComponent, computed } from 'vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import FilterSideBar from '../components/Organisms/FilterSideBar/FilterSideBar.vue';
import ProductCard from '../components/Molecules/ProductCard/ProductCard.vue';
import Pagination from '../components/Molecules/Pagination/Pagination.vue';
import { SfChip, SfIconCloseSm, SfThumbnail } from '@storefront-ui/vue';
import { SfCounter } from '@storefront-ui/vue';
import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import { useMeta } from 'vue-meta'
// import Chips
// import benq from '@/assets/images/benq.png';
// import benqth685p from '@/assets/images/products/benq-th685p-projector-500x500.png';

import { useProductsStore } from '../stores/productStore';
import NavbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';

const chipValues = ref([
  { label: 'Red', value: 'red' },
  { label: 'Blue', value: 'blue' },
  { label: 'Gray', value: 'gray' },
]);
const selectedValues = chipValues.value.map((item) => item.value);
const handleChipRemove = (index: number) => {
  chipValues.value.splice(index, 1);
};

export default defineComponent({
  setup() {
    const productsStore = useProductsStore();
    useMeta({ title: 'Products' })
    
    const products = computed(() => {
      

      if ( productsStore.filteredProducts.length < 1) {
        return productsStore.products;
      } else {
        return productsStore.filteredProducts;
      }
    });
    console.log(Object.keys(productsStore.filterCriteria), " products from products.vue");
    return {
      products, productsStore, chipValues, selectedValues, handleChipRemove
    };
  },
  components: {
    Navbar,
    NavbarBottom,
    Breadcrumbs,
    FilterSideBar,
    ProductCard,
    Pagination,
    SfChip,
    SfIconCloseSm,
    SfThumbnail,
    SfCounter,
    TrustBanner,
    Footer


  },

});

</script>