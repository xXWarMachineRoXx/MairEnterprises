<template>
    <div>
        <Navbar />
        <navbarBottom />
        <div class="mx-12 my-8 p-4">
            <Breadcrumbs class="mb-8"/>
            <div class="flex flex-col md:flex-row gap-8">
                <div class="md:w-1/2">
                    <!-- <testGallery/> -->
                    <ProductGallery :productName="currentPage" :img="product?.img ?? ''" :alt="product?.alt ?? ''" />

                </div>
                <div class="md:w-1/2">
                    <ProductDetail :productName="currentPage.toString()" :productDescription="fulldescription" :techspecs="techspecs" :price="price" :priceInt="priceInt" :rating="rating" :numberofReviews="numberofReviews"/>
                </div>
            </div>
            <Accordion/>
        </div>
        <Footer/>

    </div>
</template>

<script lang="ts" setup>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import ProductDetail from '../components/Organisms/ProductDetail/ProductDetail.vue';
// import testGallery from '../components/Molecules/testGallery/testGallery.vue';
import ProductGallery from '../components/Organisms/ProductGallery/ProductGallery.vue';
import Accordion from '../components/Molecules/Accordion/Accordion.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import { useProductsStore } from '../stores/productStore';
import { ref } from 'vue';
import navbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';
import router from '../router';

const route=router.currentRoute
const currentPage=route.value.params.productName
console.log(route.value.params.productName)
// Find the product with the matching productName
const product = useProductsStore().products.find((p) => p.productLink === currentPage);
console.log(product);
// // Store the fulldescription and techspecs
const fulldescription = ref(product?.fulldescription || '');
const techspecs = ref(product?.techspecs || {});
const price = ref((product?.price) || 0);
const priceInt = ref((product?.priceInt) || 0);
const rating = ref((product?.averageRating) || 0);
const numberofReviews = ref((product?.numberofReviews) || 0);
// const img = ref((product?.img) || 0);
// const images=ref(({product?.img,product?.alt,product?.}) || 0);

console.log("techspecs",techspecs);



</script>
