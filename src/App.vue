<template>
      <metainfo>
            <template v-slot:title="{ content }">{{ content ? `${content} | Mair Enterprises` : `Mair Enterprises` }}</template>
      </metainfo>

      <router-view />
</template>

<script lang="ts" >
import { useMeta } from 'vue-meta'
export default {
  setup () {
    useMeta({
      title: '',
      htmlAttrs: { lang: 'en', amp: true }
    })
  }
}


</script>