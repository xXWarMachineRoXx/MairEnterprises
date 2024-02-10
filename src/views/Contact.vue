<template>
    <Navbar/>
    <div class="flex flex-wrap content-center">
      <div class="pb-10 pt-5 bg-secondary-50 grow border-b-primary-500 border-b-2">
        <h1 class="text-5xl text-center">Contact Us</h1>
        <form class="contact-us ml-[20%]">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" class="!border-primary-200 bg-primary-50 " required>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" class="!border-primary-200 bg-primary-50 " required>
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" class="!border-primary-200 bg-primary-50 " required></textarea>
          </div>
          <div class="text-center">
            <button type="submit" class="!pl-10 !pr-10 !text-primary-500 !bg-primary-100 hover:!bg-primary-300 hover:!text-white">Submit</button>
          </div>
        </form>
      </div>
      <div class="flex grow justify-center items-center border-l-primary-500 border-l-2 bg-secondary-100">
        <contact/>
      </div>
    </div>
    <Footer/>
  </template>
  

<script>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import contact from '../components/Organisms/Contact/Contactinfo.vue'
export default {
    data() {
        return {
            name: '',
            email: '',
            message: ''
        };
    },
    components: {
        Navbar,
        Footer,
        contact,
    },
    methods: {
        submitForm() {
            // Handle form submission logic here
            console.log('Form submitted');
        }
    }
};
</script>

<style scoped>
.contact-us {
    max-width: 400px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 1rem;
}

label {
    display: block;
    font-weight: bold;
}

input,
textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
</style>
