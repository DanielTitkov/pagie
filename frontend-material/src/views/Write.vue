<template>
    <div class="about">
        <h1 class="secondary--text">Write!</h1>
        <v-container class="my-5">
            <!-- <Calendar /> -->
            <Writer />
        </v-container>
    </div>
</template>

<script>
import Writer from '@/components/Writer';
import Calendar from '@/components/Calendar';

export default {
    components: {
        Writer,
        Calendar
    },
    computed: {}
};
</script>
