<template>
  <div class="flex flex-col sm:flex-row !justify-center flex-wrap p-14">
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconLocalShipping size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">Nature of Business</h3>
          <h1 class="text-xl font-medium">Wholesaler</h1>
        </p>
      </div>
    </div>
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconPerson size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">Total Number of Employees</h3>
          <h1 class="text-xl font-medium">Upto 10 People</h1>
        </p>
      </div>
    </div>
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconWarehouse size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">Year of Establishment</h3>
          <h1 class="text-xl font-medium">2017</h1>
        </p>
      </div>
    </div>
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconCalendarToday size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">Annual Turnover</h3>
          <h1 class="text-xl font-medium">Rs. 50 Lakh - 1 Crore</h1>
        </p>
      </div>
    </div>
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconContactSupport size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">Legal Status of Firm</h3>
          <h1 class="text-xl font-medium">Individual - Proprietor</h1>
        </p>
      </div>
    </div>
    <div class="flex items-center sm:ml-8  basis-1/4 sm:p-5">
      <SfIconViewList size="2xl" class="text-secondary-200"/>
      <div class="pad">
        <p class="leading-5">
          <h3 class="text-base text-gray-600">GST Number</h3>
          <h1 class="text-xl font-medium">06ABZPM9198B1ZX</h1>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { SfIconLocalShipping } from '@storefront-ui/vue';
import { SfIconPerson } from '@storefront-ui/vue';
import { SfIconWarehouse } from '@storefront-ui/vue';
import { SfIconCalendarToday } from '@storefront-ui/vue';
import { SfIconContactSupport } from '@storefront-ui/vue';
import { SfIconViewList } from '@storefront-ui/vue';


</script>

<style scoped>
.pad {
  margin-left: 1.5rem;
  margin-top: 7px;
}
</style>
