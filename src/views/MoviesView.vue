<script setup>
import { ref, onMounted, defineProps, computed } from "vue";

let movies = ref([]);

const errors = ref([]);

const loading = ref(true);

const props = defineProps({
  isDarkmode: Boolean
});

/**
 * A computed property that dynamically assigns CSS classes to a movie element
 * based on the `isDarkmode` prop. This allows for theme switching between
 * dark and light modes.
 *
 * Classes:
 * - 'movie-dark-theme': Applied when `isDarkmode` is true.
 * - 'movie-light-theme': Applied when `isDarkmode` is false.
 *
 * @returns {Object} An object containing the CSS class mappings.
 */
const movieClass = computed(() => {
  return {
    'movie-dark-theme': props.isDarkmode,
    'movie-light-theme': !props.isDarkmode,
  };
});

const fetchMovies = () => {

    fetch('/api/v1/movies', {
        method: 'GET'
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors){
                errors.value = data.errors;
            } else{
                movies.value = data.movies;
            }
        })
        .catch(function (error) {
            errors.value = ["An unexpected error occurred."];
            console.error("Fetch error: ", error);
        })
        .finally(() => {
            loading.value = false;
        });
    
}

onMounted(() => {
    setTimeout (() => {
        fetchMovies(); 
    }, 1000);
});

</script>



<template>

<div class="movie-list">
   
    <h1 class="movie-heading">Movies</h1>
    <!--**
     * Conditional rendering block for displaying a loading state when movies are being fetched or the movies array is empty.
     * 
     * Props/Variables:
     * - `movies`: An array containing movie data. If its length is 0, the loading state is displayed.
     * - `loading`: A boolean indicating whether the movies are currently being loaded.
     * 
     * Behavior:
     * - If `movies.length === 0` or `loading` is true, the loading state is shown.
     * - The `movie-load` class is always applied to the container.
     * - If `isDarkmode` is false, an additional `movie-load-light-theme` class is applied for light mode styling.
     * 
     * Content:
     * - Displays a "Loading movies..." message.
     * - Includes a spinner element for visual feedback during loading.
     *-->
    <div v-if="movies.length === 0 || loading" class="movie-load" :class="!isDarkmode ? 'movie-load movie-load-light-theme' : 'movie-load'">
        <p>Loading movies...</p>
        <div class="spinner"></div>
    </div>
    <div v-else class="movies-listed">
        <div v-for="movie in movies" :key="movie.id" class="movie" :class="movieClass">
            <img v-if="movie.poster" :src="`http://localhost:5173${movie.poster}`" alt="Movie Poster" class="movie-img" width="450">
            <div class="text-content">
                <h2 class="movie-title">{{ movie.title }}</h2> 
                <p class="movie-description">{{ movie.description }}</p>
            </div>
        </div>
    </div>
</div>

</template>


<style scoped>

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #007bff;
  border-radius: 50%;
  animation: spin 10s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.movie-heading {
    text-align: left;
    margin-left: 50px;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    align-items: start;
}

.movie-list {
  text-align: left;
}

.movies-listed {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Create three columns per row */
  gap: 30px 40px; /* Space between the items */
  width: 650px;
  margin-left: 50px;
}
.movie {
  display: grid;
  grid-template-columns: 190px 1fr; /* Image takes up 190px, text takes the remaining space */
  align-items: flex-start;  /* Align the content to the top */
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  width: 450px;
  height: 250px;
  transition: all 0.3s ease-in-out;
}


.movie-light-theme {
  background: #ece8e8;
}

.movie-dark-theme {
  background: #D1D8E0;
}

.movie-light-theme:hover {
  background: white ;
  transform: scale(1.05);
  box-shadow: 0px 0px 10px rgb(146, 144, 144) ;
  border-color: #817e7e96 ;
}

.movie-dark-theme:hover {
  transform: scale(1.05); /* Slightly enlarges the card */
  box-shadow: 0px 0px 10px #ffcc00; /* Increases shadow */
  border-color: #817e7e96; /* Changes border color */
  background: #ffcc00 ;
}


.movie-img {
  width: 170px; 
  height: 248px;
  border-top-left-radius: 8px;  /* Curves the top-left corner */
  border-bottom-left-radius: 8px;
}

.movie-title {
  font-size: 20px;
  margin-bottom: 10px;
  font-weight: bold;
  text-align: left; 
  margin-left: 0px; /* Explicitly align the title to the left */
}

.movie-description {
  font-size: 15px;
  text-align: left;  /* Align text to the left */
  margin-top: 10px;  /* Add some space between the title and description */
}

.text-content {
    width: 250px;
    padding-top: 10px;
    text-align: left;
    justify-content: left;
    color: black;
}

.movie-load {
    font-family: 'Helvetica','Roboto','Open Sans';
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    background: #121d33;
    color: #E0E6F0;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100%;
    z-index: 100;
}

.movie-load-light-theme {
  background: white;
  color: black;
}
</style>