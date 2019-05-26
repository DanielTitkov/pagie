<template>
    <div class="calendar">
        <v-layout row wrap justify-center>
            <v-flex xs12 md10 lg8 xl6 my-3>
                <span
                    class="calendar-item-wrapper"
                    v-for="date in datesData"
                    v-bind:key="date.date"
                >
                    <router-link
                        :to="{
                            name: 'history',
                            params: { dateslug: date.date }
                        }"
                    >
                        <v-tooltip top>
                            <template v-slot:activator="{ on }">
                                <v-icon
                                    :color="selectColor(date)"
                                    v-on="on"
                                    :class="{ textPresent: date.textPresent }"
                                    >fiber_manual_record</v-icon
                                >
                            </template>
                            <span>{{ date.date | toReadableDate }}</span>
                        </v-tooltip>
                    </router-link>
                </span>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selectedDate: null,
            dateslug: this.$route.params.dateslug
        };
    },
    computed: {
        datesData() {
            return this.$store.getters.datesData;
        },
        currentDate() {
            return this.$store.getters.date;
        }
    },
    methods: {
        selectColor(dateObj) {
            return dateObj.date == this.currentDate
                ? 'secondary'
                : dateObj.textPresent
                ? 'primary'
                : 'grey';
        },
        ifSelected(dateObj) {
            return dateObj.date == this.dateslug ? true : false;
        }
    },
    created() {
        this.$store.dispatch('getDatesData');
    }
};
</script>

<style scoped>
.textPresent {
}
.calendar {
}
.calendar-item-wrapper:last-child {
    /* border: 2px solid red;
    background-color: black; */
}
.router-link-active {
    /* display: inline-block;
    border-radius: 50%;
    border: 1px solid blue; */
}
</style>
