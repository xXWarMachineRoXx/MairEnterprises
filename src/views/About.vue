
<template>
    <Navbar/>
    <div class="about">
        <h1 class="text-5xl text-center">About Us</h1>
        <p>Welcome to our website! We are a team of passionate individuals dedicated to providing high-quality products and services.</p>
        <p>Our mission is to exceed customer expectations and deliver innovative solutions that drive success.</p>
        <p>Feel free to explore our website and learn more about our company and the services we offer.</p>
    </div>
    <Footer/>
</template>

<script>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Footer from '../components/Organisms/Footer/Footer.vue'
export default {
    name: 'About',
    components: {
        Navbar,
        Footer
    }
}


</script>

<style scoped>
.about {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}
</style>