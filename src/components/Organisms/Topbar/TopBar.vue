<template>
    <SfButton @click="call" class="w-full rounded-none !bg-primary-300 !text-primary-800">  <Component :is="SfIconCall" /> Call us at: +91 794 296 9133 </SfButton>
</template>
  
<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import { SfIconCall } from '@storefront-ui/vue';

function call() {
  location.href = "tel:+917942969133";
}

</script>