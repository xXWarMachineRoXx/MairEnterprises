
<template>
    <Navbar/>
    <navbarBottom class="md:hidden lg:hidden sm:hidden"/>
    <!-- <Category/> -->
    <div class="about   md:!mx-auto xs:!mx-20">
        <h1 class="text-5xl text-center ">About Us</h1>
        <!-- <p>Welcome to our website! We are a team of passionate individuals dedicated to providing high-quality products and services.</p>
        <p>Our mission is to exceed customer expectations and deliver innovative solutions that drive success.</p>
        <p>Feel free to explore our website and learn more about our company and the services we offer.</p> -->
        <p>Established in the year 2017, Gurgaon, Haryana "Mair Enterprises" are a Proprietorship are engaged Wholesale Of InFocus Projector, BenQ Projector, Epson Projector ViewSonic Projector Etc.</p>
    </div>
    
    <Factsheet class="p-4 xs:!ml-20 !mx-auto mb-6"/>   
    <Category/>
    <TrustBanner/>
    <Footer/>
</template>

<script setup>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import Category from '../components/Organisms/Categories/Categories.vue';
import Factsheet from '../components/Organisms/Factsheet/Factsheet.vue'
import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
import navbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';



</script>

<style scoped>
.about {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}
</style>