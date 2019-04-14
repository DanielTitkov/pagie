<template>
    <div class="history">
        <h1 class="grey--text">History</h1>
        <v-container class="my-5">
            <AllTexts v-if='!dateslug' />
            <Calendar v-if='dateslug' />
            <Writer v-if='dateslug' :dateslug="dateslug" />
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
        };
    },
    components: {
        Writer,
        Calendar,
        AllTexts: () => import('@/components/AllTexts.vue')
    },
    created() {
        this.$store.dispatch('getDate');
    },
    computed: {
        date() {
            return this.$store.getters.date;
        }
    },
    beforeRouteUpdate(to, from, next) {
        this.dateslug = to.params.dateslug;
        if (this.dateslug == this.date) {
            this.$router.push('/');
        }
        next();
    },
    watch: {
        $route(to, from) {
            this.dateslug = to.params.dateslug;
        }
    }
};
</script>
