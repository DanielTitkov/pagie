<template>
    <div class="about">
        <h1 class="secondary--text">Write!</h1>
        <v-container class="my-5">
            <Writer />
        </v-container>
    </div>
</template>

<script>
import Writer from '@/components/Writer';

export default {
    components: {
        Writer
    },
    computed: {}
};
</script>
