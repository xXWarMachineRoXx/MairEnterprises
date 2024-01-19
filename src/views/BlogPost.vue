<template >
  <TopBar />
  <Navbar class="" />

  <!-- Add padding to the parent container instead of margin to the child -->
  <div class="bg-primary-100 pt-8">
    <div class="prose text-pretty p-4 container mx-auto bg-white shadow-lg rounded-lg max-w-screen-xl">
      <div class="">
        <vue-showdown :markdown="blogContent" />
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
import { useRoute } from 'vue-router';



export default defineComponent({
  components: {
    TopBar,
    Navbar,
    Footer,
    TrustBanner,
    Newsletter
  },
  setup() {
    const route = useRoute();
    const blogContent = ref('');

    onMounted(async () => {
      const blogName = route.params.blogName as string;
      fetch(`/src/blogs/${blogName}.md`)
        .then(response => response.text())
        .then(data => {
          blogContent.value = data;
        })
        .catch(error => console.error('Error fetching markdown:', error));
    });

    return { blogContent };
  },
});
</script>
  