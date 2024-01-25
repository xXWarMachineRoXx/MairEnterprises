<template>
   <TopBar/>
   <Navbar/>
   <div class="mx-12 my-8 p-4">
       <Breadcrumbs/>
       <div class="text-center">
            <h1 class="font-bold text-4xl">Blog</h1>
            <p class="text-lg">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.</p>
       </div>
    </div>
     
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import TopBar from '../components/Organisms/Topbar/TopBar.vue';
  import Navbar from '../components/Organisms/Navbar/Navbar.vue';
  import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
  
  
  export default defineComponent({
    data() {
        return {
           
        };
    },
    components: { Navbar,TopBar,Breadcrumbs }
  });
  </script>
  