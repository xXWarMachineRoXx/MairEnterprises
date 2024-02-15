<template>
    <SfButton @click="call" class="w-full rounded-none !bg-primary-300 !text-primary-800">  <Component :is="SfIconCall" /> Call us at: +91 981 015 9599  </SfButton>
</template>
  
<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import { SfIconCall } from '@storefront-ui/vue';

function call() {
  location.href = "https://wa.me/919810159599";
}

</script>