
<template>
    <div class="contact-us">
        <h1 class="text-5xl">Contact Us</h1>
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name"  required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email"  required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message"  required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            email: '',
            message: ''
        };
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
