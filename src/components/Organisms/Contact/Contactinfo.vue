<template>
  <div class="flex flex-wrap justify-center items-center">
    <!-- Address section -->
    <div class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-700 border-2 !m-5 max-w-[90%] md:max-w-[70%]">
      <SfIconLocationOnFilled size="2xl" class="text-primary-700" />
      <p class="prose-lg max-w- font-semibold pl-2.5 text-primary-900 p-4">First Floor, Office No. 5A, Block-A, Omaxe Gurgaon Mall, Sohna Road, Sector 49, Gurgaon, Gurugram-122018, Haryana, India</p>
    </div>
    
    <!-- Contact section -->
    <div @click="call" class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-700 border-2 !m-5 items-center text-xl max-w-[90%] md:max-w-[70%]">
      <!-- Phone number -->
      <div class="flex items-center basis-1/2 border-r-2 border-secondary-700 pr-5 md:pr-0">
         <img src="https://cdn-icons-png.flaticon.com/512/3670/3670051.png" alt="whatsapp" class="w-10 h-10" />
        <!-- <SfIconCall size="2xl" class="text-primary-700" /> -->
        <p class="prose-lg justify-normal font-semibold pl-2.5 text-primary-900">+91 981 015 9599 </p>
      </div>
      <!-- Person's name -->
      <div class="flex items-center basis-1/2 pl-5 md:pl-0">
        <SfIconPerson size="2xl" class="text-primary-700 ml-5" />
        <p class="prose-lg justify-normal font-semibold pl-2.5 text-primary-900 ml-2"> Mr. Rajendra Mair</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { SfIconLocationOnFilled, SfIconPerson } from '@storefront-ui/vue';
// import whatsapplogo from  'https://cdn-icons-png.flaticon.com/512/3670/3670051.png';

function call() {
  location.href = "https://wa.me/919810159599";
}
</script>
