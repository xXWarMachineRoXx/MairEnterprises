<template>
  <div class="flex flex-wrap justify-center items-center">
    <!-- Address section -->
    <div class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-700 border-2 !m-5 max-w-[90%] md:max-w-[70%]">
      <SfIconLocationOnFilled size="2xl" class="text-primary-700" />
      <p class="leading-4 justify-normal max-w-96 font-semibold pl-2.5 text-primary-900">First Floor, Office No. 5A, Block-A, Omaxe Gurgaon Mall, Sohna Road, Sector 49, Gurgaon, Gurugram-122018, Haryana, India</p>
    </div>
    
    <!-- Contact section -->
    <div @click="call" class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-700 border-2 !m-5 items-center text-xl max-w-[90%] md:max-w-[70%]">
      <!-- Phone number -->
      <div class="flex items-center basis-1/2 border-r-2 border-secondary-700 pr-5 md:pr-0">
        <SfIconCall size="2xl" class="text-primary-700" />
        <p class="leading-4 justify-normal max-w-72 font-semibold pl-2.5 text-primary-900">+91 981 015 9599 </p>
      </div>
      <!-- Person's name -->
      <div class="flex items-center basis-1/2 pl-5 md:pl-0">
        <SfIconPerson size="2xl" class="text-primary-700" />
        <p class="leading-4 justify-normal max-w-72 font-semibold pl-2.5 text-primary-900">Rajendra Mair (Owner)</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { SfIconLocationOnFilled, SfIconCall, SfIconPerson } from '@storefront-ui/vue';
function call() {
  location.href = "tel:+919810159599";
}
</script>
