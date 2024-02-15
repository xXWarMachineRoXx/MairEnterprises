<template>
  <div id="mc_embed_shell" class="aspect-auto">
    <iframe  class="iframe_container" seamless src="https://us17.list-manage.com/contact-form?u=9f204b67f189919cd6234ce1b&form_id=607ecc7b4616d3a1993c463389c3172f" frameborder="0" style="border: none;"></iframe>
  </div>
</template>

<script>
export default {
  // Component logic
};
</script>

<style scoped>
/* Component styles */
.iframe_container {
  min-width: 500px !important;
  min-height: 1000px !important;
  width: 100%;
}

@media (min-width: 768px) {
  /* For md breakpoint */
  .iframe_container {
    min-width: 600px !important; /* Adjust as needed */
  }
}

@media (min-width: 992px) {
  /* For lg breakpoint */
  .iframe_container {
    min-width: 700px !important; /* Adjust as needed */
  }
}

@media (min-width: 1200px) {
  /* For xl breakpoint */
  .iframe_container {
    min-width: 800px !important; /* Adjust as needed */
  } 
}
</style>
