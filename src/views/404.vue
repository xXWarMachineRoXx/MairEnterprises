<template>
    <TopBar />
    <Navbar />
    
        <div class="relative min-h-[600px]">
            <picture>
                <source srcset="https://storage.googleapis.com/sfui_docs_artifacts_bucket_public/production/hero-bg.png"
                    media="(min-width: 768px)" />
                <img src="https://storage.googleapis.com/sfui_docs_artifacts_bucket_public/production/hero-bg-mobile.png"
                    class="absolute w-full h-full z-[-1] md:object-cover" alt="hero" />
            </picture>
            <div class="md:flex md:flex-row-reverse md:justify-center max-w[1536px] mx-auto md:min-h-[600px]">
                <div class="flex flex-col md:basis-2/4 md:items-stretch md:overflow-hidden">
                    <img src="https://storage.googleapis.com/sfui_docs_artifacts_bucket_public/production/hero-headphones.png"
                        alt="Headphones" class="h-full object-cover object-left" />
                </div>
                <div class="p-4 md:p-10 md:max-w-[768px] md:flex md:flex-col md:justify-center md:items-start md:basis-2/4">
                    <p
                        class="typography-text-xs md:typography-text-sm font-bold tracking-widest text-neutral-500 uppercase">
                        Cannot find what you are looking for?
                    </p>
                    <h1 class="typography-display-2 md:typography-display-1 md:leading-[67.5px] font-bold mt-2 mb-4">
                        Try our search
                    </h1>
                    <p class="typography-text-base md:typography-text-lg">
                        We have over 1000 products in our store. You will definitely find something for yourself.
                    </p>
                    <div class="flex flex-col md:flex-row gap-4 mt-6">
                        <SfButton size="lg"> Go Back </SfButton>
                        <SfButton size="lg" variant="secondary" class="bg-white" onclick="">  Home </SfButton>
                    </div>
                </div>
            </div>
        </div>
    
</template>


<script lang="ts" setup>
import { SfButton } from '@storefront-ui/vue';
import TopBar from '../components/Organisms/Topbar/TopBar.vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import { useMeta } from 'vue-meta';

useMeta({
    title: '404 Not Found'
})

</script>
