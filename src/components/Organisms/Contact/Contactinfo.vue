<template>
    <div class="flex flex-wrap justify-center items-center">
        <div class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-200 border-2 !m-5 max-w-[70%]">

      <SfIconLocationOnFilled size="2xl" class="" />
        <p class="leading-4 justify-normal max-w-96 font-semibold pl-2.5">First Floor, Office No. 5A, Block-A, Omaxe Gurgaon Mall,Sohna Road, Sector 49, Gurgaon, Gurugram-122018, Haryana, India</p>
        </div>
        <div class="flex bg-primary-50 p-5 grow basis-1/2 border-secondary-200 border-2 !m-5 items-center  text-xl max-w-[70%]">
        <div class="flex items-center basis-1/2 border-r-2 border-secondary-200">
      <SfIconCall size="2xl" class="" />
        <p class="leading-4 justify-normal max-w-72 font-semibold pl-2.5">12345678901</p>
        </div>
        <div class="flex items-center basis-1/2 pl-5">
            <SfIconPerson size="2xl" class="" />
            <p class="leading-4 justify-normal max-w-72 font-semibold pl-2.5">Rajendra Mair (Owner)</p>
</div>
        </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { SfIconLocationOnFilled } from '@storefront-ui/vue';
  import { SfIconCall } from '@storefront-ui/vue';
  import { SfIconPerson } from '@storefront-ui/vue';



  </script>
  