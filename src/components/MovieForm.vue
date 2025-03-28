<script setup>
import { ref, onMounted, defineEmits, nextTick } from 'vue';


/**
 * Emits a custom event named 'flashMessage'.
 * This event can be used to send a flash message to a parent component.
 * 
 * Usage:
 * - The parent component should listen for the 'flashMessage' event.
 * - The event can carry a payload if needed, such as a message string or object.
 * 
 * Example:
 * <MovieForm @flashMessage="handleFlashMessage" />
 */
const emit = defineEmits(['flashMessage']);

let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log("CSRF Token: ",data);
            csrf_token.value = data.csrf_token;
        })
        .catch((error) => {
            console.log("Error: ",error);
        });
}

onMounted(() => {
    getCsrfToken();
});

const title = ref('');
const description = ref('');
const poster = ref(null);
const fileInput = ref(null);
const success_message = ref('');
const errors = ref([]);

/**
 * Handles the change event for a file input element.
 * Updates the `poster` reactive variable with the selected file.
 *
 * @param {Event} event - The file input change event.
 */
const handleFileChange = (event) => {
    poster.value = event.target.files[0];
};

const saveMovie = () => {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    errors.value = [];
    success_message.value = '';

    fetch('/api/v1/movies', {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors){
                errors.value = data.errors;
                emit('flashMessage',errors);
            } else{
                success_message.value = "Movie Successfully Added!!!";
                /**
                 * Resets the form fields for the movie form component.
                 * - Clears the `title` and `description` input fields by setting their values to an empty string.
                 * - Resets the file input field by setting its value to `null` using Vue's `nextTick` to ensure
                 *   the DOM is updated before making the change.
                 */
                title.value = '';
                description.value = '';
                nextTick(() => {
                    fileInput.value.value = null;
                })
                /**
                 * Emits a 'flashMessage' event with a success message.
                 * 
                 * @event flashMessage
                 * @param {string} success_message - The message to be displayed as a flash notification.
                 */
                emit('flashMessage',success_message);
            }
        })
        .catch(function (error) {
            emit('refreshPage');
            console.error("Fetch error: ", error);
        });
}

</script>



<template>
    <div class="movie-form-div">

        <!--**
         * This section of the code defines a transition effect for a success message.
         * 
         * - The `<transition>` element is used to apply a named transition effect ("fade") 
         *   when the success message is displayed or removed.
         * - The `success_message` variable is expected to hold the text of the success 
         *   message, which is displayed inside the `<div>` element.
         *-->
        <transition name="fade">
            <div v-if="success_message" class="success-message">
                {{ success_message }}
            </div>
        </transition>

        <!--**
         * This section of the Vue component handles the display of error messages using a transition effect.
         * 
         * - The `v-if="errors.length"` directive ensures that the error message block is only rendered if there are errors in the `errors` array.
         * - Inside the `<ul>` element, a `<li>` is rendered for each error in the `errors` array using the `v-for` directive.
         * - The `:key="index"` binds a unique key to each `<li>` element based on its index in the array, which helps Vue efficiently update the DOM.
         *-->
        <transition name="fade">
            <div v-if="errors.length" class="error-message">
                <ul>
                    <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
                </ul>
            </div>
        </transition>

        <form id="movieForm" @submit.prevent="saveMovie" class="movie-form" enctype="multipart/form-data">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Title</label>
                <input id="title" type="text" name="title" v-model="title" class="form-control" />
            </div>
    
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea id="description" name="description" v-model="description" class="form-control" ></textarea>
            </div>
    
            <div class="form-group mb-3">
                <div class ="poster">
                    <label for="poster" class="form-label">Poster</label>
                    <label for="poster-type" class="form-label poster-type">(PNG,JPG,JPEG)</label>
                </div>
                <!--
                    The `@change` event is used to trigger the `handleFileChange` method whenever a file is selected. The 
                    `ref="fileInput"` attribute provides a reference to this input element for programmatic access.
                -->
                <input id="poster" name="poster" type="file" @change="handleFileChange" ref="fileInput" accept="image/png, image/jpeg"  class="form-control" />
            </div>
    
        <button type="submit" name="submit" class="btn btn-primary">Submit</button>
        </form>

    </div>
  </template>

<style scoped>
.success-message {
    color: green;
    background-color: #d4edda;
    padding: 10px;
    border-radius: 5px;
    width: 15%;
    top: 100px;
    right: 45px;
    text-align: center;
    position: fixed;
}

.error-message {
    color: red;
    background-color: #f8d7da;
    padding: 10px;
    padding-top: 20px;
    padding-left: 0px;
    margin-bottom: 10px;
    border-radius: 5px;
    top: 70px;
    right: 45px;
    position: fixed;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 26%;
    min-height: 8%;
    height: auto;
}

.fade-leave-active {
  transition: opacity 1s ease-in-out;
}

.fade-leave-to {
  opacity: 0;
}

textarea, textarea:focus{
    width: 100%; 
    height: 200px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background-color: #fcfcfcdc;
    color: #070000;
    font-weight: bold;
}


textarea:hover:not(:focus) {
    border-color: #292a2c; /* Darker border on hover */
    box-shadow: 0 0 5px rgba(247, 245, 245, 0.788); /* Slight glow effect */
    background-color: #fcfcfcab;
}


input, input:focus {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc; 
    background-color: #fcfcfcdc;
    color: #070000;
    font-weight: bold;
}

#poster::file-selector-button {
    background-color: #1b1a1a41;
}

input:hover:not(:focus) {
    border-color: #292a2c; /* Darker border on hover */
    box-shadow: 0 0 5px rgba(247, 245, 245, 0.788); /* Slight glow effect */
    background-color: #fcfcfcab;
}


label {
    font-weight: bold;
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 18px;
    padding-top: 10px;
}

.form-control {
    font-family: 'Helvetica','Roboto','Open Sans';
}

.poster-type {
    font-size: 14px;
    margin-left: 10px;
}

.btn-primary {
    margin-top: 30px;
    width: 100px;
}
</style>