<template class="!bg-primary-500">
    <Navbar />
    <div class="mx-12 my-8 p-4">
        <Breadcrumbs />
        <h1 class="font-bold text-4xl"> Browse Category </h1>
        <div class="flex gap-6">
            <FilterSideBar />
            <div class="flex flex-col gap-8">
                <h2 class="font-bold text-lg"> All Products </h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                    <ProductCard v-for="product in products" :key="product.id" :img="product.img" :alt="product.alt"
                        :productName="product.productName" :price="product.price" :description="product.description"
                        :numberofReviews="product.numberofReviews" :category="product.category"
                        :canWishlist="product.canWishlist" :averageRating="product.averageRating"
                        :productLink="product.productLink" />
                </div>
                <Pagination />
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
import { defineComponent,computed } from 'vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import FilterSideBar from '../components/Organisms/FilterSideBar/FilterSideBar.vue';
import ProductCard from '../components/Molecules/ProductCard/ProductCard.vue';
import Pagination from '../components/Molecules/Pagination/Pagination.vue';
// import benq from '@/assets/images/benq.png';
// import benqth685p from '@/assets/images/products/benq-th685p-projector-500x500.png';

import { useProductsStore } from '../stores/productStore';

export default defineComponent({
    data() {
        const productsStore = useProductsStore();
        
        return {
            products: computed(() => productsStore.filteredProducts ) 
        };
    },

    components: { Navbar, Breadcrumbs, FilterSideBar, ProductCard, Pagination }
});

</script>