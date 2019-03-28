<template>
    <div class="about">
        <h1 class="secondary--text">Write!</h1>
        <v-container class="my-5">
            <!-- <Calendar /> -->
            <Writer :dateslug='dateslug' />
        </v-container>
    </div>
</template>

<script>
import Writer from '@/components/Writer';
import Calendar from '@/components/Calendar';

export default {
    data() {
        return {
            dateslug: this.$route.params.dateslug
        }
    },
    components: {
        Writer,
        Calendar
    }
};
</script>
