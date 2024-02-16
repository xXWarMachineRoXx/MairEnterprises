<template>
  <TopBar />
  <Navbar class="" />
  <navbarBottom class="md:hidden lg:hidden sm:hidden"/>
  
  <div class="bg-primary-100 pt-8">
    <div class="prose text-pretty p-4 container mx-auto bg-white shadow-lg rounded-lg max-w-screen-xl">
      <Breadcrumbs class=""/>
      <div class="ml-8">
        <!-- Render the imported blog component directly -->
        <component :is="currentBlogComponent" />
      </div>
    </div>
  </div>
  
  <Newsletter />
  <TrustBanner />
  <Footer />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import TopBar from '../components/Organisms/Topbar/TopBar.vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import Newsletter from '../components/Organisms/NewsLetter/Newsletter.vue';
import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import navbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';
import { useRoute } from 'vue-router';
import { defineAsyncComponent } from 'vue'

export default defineComponent({
  components: {
    TopBar,
    Navbar,
    Footer,
    TrustBanner,
    Newsletter,
    Breadcrumbs,
    navbarBottom
  },
  setup() {
    const currentBlogComponent = ref(null);

    onMounted(async () => {
      const route = useRoute();
      const blogName = route.params.blogName as string;

      try {
        // Dynamically import the Vue component based on the blog name
        const BlogComponent = defineAsyncComponent(() => import(`../blogs/${blogName}.vue`));

        currentBlogComponent.value = BlogComponent;
        console.log('Blog component loaded:', BlogComponent);
      } catch (error) {
        // If the blog component is not found, load the default blog component
        console.error('Error loading blog component:', error);
      }
    });

    return { currentBlogComponent };
  }
});
</script>
