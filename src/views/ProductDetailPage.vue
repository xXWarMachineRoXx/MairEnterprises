<template>
    <div>
        <Navbar />
        <div class="mx-12 my-8 p-4">
            <Breadcrumbs class="mb-8"/>
            <div class="flex gap-8">
                <div class="col ">
                    <ProductGallery :productName="$route.params.productName" />
                </div>
                <div class="col ">
                    <ProductDetail :productName="$route.params.productName" />
                </div>
            </div>
            <Accordion/>
        </div>
    </div>
</template>

<script lang="ts" setup>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import ProductDetail from '../components/Organisms/ProductDetail/ProductDetail.vue';
import ProductGallery from '../components/Organisms/ProductGallery/ProductGallery.vue';
import Accordion from '../components/Molecules/Accordion/Accordion.vue';

</script>
