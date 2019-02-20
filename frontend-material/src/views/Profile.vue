<template>
    <div class="about">
        <h1 class="grey--text">Profile</h1>
        <v-container class="my-5">
            <v-layout row wrap></v-layout>
        </v-container>
    </div>
</template>

<script>
export default {
    data() {
        return {
            drawer: false,
            links: [{ icon: 'favorite', text: 'Write!', route: '/' }]
        };
    }
};
</script>
