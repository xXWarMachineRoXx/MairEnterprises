<template>
    
    <section class="benq-65-inch-interactive-panel-section">
        <img src="@/assets/images/products/smart-board.webp" alt="BenQ 65-inch Interactive Panel"
        class="w-full h-auto" />
        <h2>Best Interactive Panel: BenQ 65-inch Interactive Panel</h2>
        <p>Designed to revolutionize the way we interact with technology, the BenQ 65-inch Interactive Panel is a
            state-of-the-art display that offers unparalleled functionality and versatility. With its intuitive touch
            capabilities and seamless integration with various devices, it's an ideal solution for educational and
            professional settings alike.</p>
            <div class="video-container">
            <iframe  src="https://www.youtube.com/embed/zTGvIGDInxE?si=ZoxAgbzRo-U0PKIz&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>
            <h3>Pros:</h3>
        <ul>
            <li>Intuitive touch functionality</li>
            <li>Seamless device integration</li>
            <li>High-quality display</li>
        </ul>
        <h3>Cons:</h3>
        <ul>
            <li>Pricey compared to traditional displays</li>
            <li>Requires compatible devices for full functionality</li>
        </ul>
        <p>The BenQ 65-inch Interactive Panel is a game-changer in the realm of interactive displays, offering a
            user-friendly experience and exceptional performance. Whether you're a teacher, presenter, or business
            professional, this interactive panel is sure to elevate your presentations and collaborations to new heights.</p>
    </section>

</template>

<script setup>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import navbarBottom from '../components/Organisms/NavbarBottom/navbarBottom.vue';

import TrustBanner from '../components/Organisms/TrustBanner/TrustBanner.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
</script>

<style scoped>
.video-container {
    width: 100%; /* Set the width of the container */
    max-width: 560px; /* Set the maximum width of the container if needed */
    margin: 0 auto; /* Center the container horizontally */
}

.video-container iframe {
    width: 100%; /* Make the iframe fill the width of its container */
    height: 300px; /* Allow the iframe to adjust its height accordingly */
}
</style>