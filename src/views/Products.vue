<template class="!bg-primary-500">
  <Navbar/>
  <Breadcrumbs/>
  <FilterSideBar/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import FilterSideBar from '../components/Organisms/FilterSideBar/FilterSideBar.vue';
interface Product {
  id: number;
  name: string;
}

export default defineComponent({
    data() {
        return {
            products: [
                { id: 1, name: 'Product 1' },
                { id: 2, name: 'Product 2' },
                { id: 3, name: 'Product 3' },
                // Add more products here as needed
            ] as Product[]
        };
    },
    components: { Navbar }
});
</script>
