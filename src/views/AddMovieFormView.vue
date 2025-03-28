<script setup>
import MovieForm from '@/components/MovieForm.vue';

/**
 * Displays a temporary flash message by clearing the provided prompt value after 5 seconds.
 * 
 * @param {Ref<string | string[]>} prompt - A Vue ref object containing either a string or an array of strings.
 *                                          If it's an array, it will be cleared to an empty array.
 *                                          If it's a string, it will be cleared to an empty string.
 */
const flashMessage = (prompt) => {
    setTimeout(() => {
        if (Array.isArray(prompt)) {
            prompt.value = [];
        } else {
            prompt.value = '';
        }
  }, 5000);
}
</script>

<template>
    <div class="movie-form-view">
        <h1 class="add-movie">Add a New Movie</h1>
        <!-- 
            This line of code integrates the `MovieForm` component into the `AddMovieFormView` Vue component.
            - The `@flashMessage` directive listens for the `flashMessage` custom event emitted by the `MovieForm` component.
            - When the `flashMessage` event is triggered, it calls the `flashMessage` method or handler defined in the parent component.
            - This setup is typically used to display notifications or messages to the user after certain actions, such as successfully adding a movie.
        -->
        <MovieForm @flashMessage="flashMessage"/>
    </div>
</template>

<style scoped>
.movie-form-view {
    margin-left: 50px;
    width: 94%;
}

.add-movie {
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    align-items: start;
}

</style>
