<template>
    <div class="about">
        <h1 class="secondary--text">Write!</h1>
        <v-container class="my-5">
            <Calendar />
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
    },
    created() {
        this.$store.dispatch('getDate');
    },
    computed: {
        date() {
            return this.$store.getters.date;
        },
    },
    beforeRouteUpdate (to, from, next) {
        this.dateslug = to.params.dateslug;
        if (this.dateslug == this.date) {
            this.$router.push('/');
        }
        next();
    }
};
</script>
