<template>
    <SfButton class="w-full rounded-none !bg-primary-300 !text-primary-800">  <Component :is="SfIconCall" /> Call for best deals <a href="tel:+917942969133">+91 794 296 9133</a> </SfButton>
</template>
  
<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import { SfIconCall } from '@storefront-ui/vue';


</script>