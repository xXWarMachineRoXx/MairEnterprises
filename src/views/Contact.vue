<template>
    <Navbar />

    <div class="flex flex-wrap content-center lg:!p-10">
        <div class="pb-10 pt-5 bg-secondary-50 grow border-b-primary-500 border-b-2">
            <Form />
        </div>
        <div class="flex grow justify-center items-center border-l-primary-500 border-l-2 bg-secondary-100">
            <contact />
        </div>

    </div>
    <Footer />
</template>
  

<script>
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Footer from '../components/Organisms/Footer/Footer.vue';
import contact from '../components/Organisms/Contact/Contactinfo.vue';
import Form from '../components/Organisms/Contact/contactform.vue';
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
        Form,
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
