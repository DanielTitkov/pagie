<template>
    <div class="AllTexts">
        <h3>{{ status }}</h3>
        <v-data-table
            flat
            :headers="tableHeaders"
            :items="texts"
            :rows-per-page-items="tablePageItems"
        >
            <template v-slot:items="props">
                <td class="title">
                    <router-link
                        class="date-link"
                        :to="{
                            name: 'history',
                            params: { dateslug: props.item.date }
                        }"
                        >{{ props.item.date | toReadableDate }}</router-link
                    >
                </td>
                <td class="text-xs-right title">{{ props.item.words }}</td>
                <td class="text-xs-right title">
                    <router-link
                        :to="{
                            name: 'history',
                            params: { dateslug: props.item.date }
                        }"
                        ><v-icon color="primary">remove_red_eye</v-icon>
                    </router-link>
                </td>
            </template>
        </v-data-table>
    </div>
</template>

<script>
import axios from 'axios';
import config from '@/config';

export default {
    data() {
        return {
            tablePageItems: [
                10,
                30,
                50,
                { text: '$vuetify.dataIterator.rowsPerPageAll', value: -1 }
            ],
            tableHeaders: [
                {
                    text: 'Date',
                    align: 'left',
                    value: 'date',
                    class: 'title',
                    width: '70%'
                },
                {
                    text: 'Words',
                    value: 'words',
                    align: 'right',
                    class: 'title'
                },
                {
                    text: 'View',
                    value: 'view',
                    align: 'right',
                    class: 'title',
                    sortable: false
                }
            ],
            texts: [],
            loading: true,
            status: ''
        };
    },
    methods: {
        fetchTexts() {
            this.loading = true;
            this.status = 'loading...';
            axios
                .get(config.API_URL + 'texts', {
                    headers: {
                        Authorization: `Bearer ${
                            this.$store.getters.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    this.texts = response.data;
                    this.loading = false;
                    this.status = '';
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    created() {
        this.fetchTexts();
    }
};
</script>

<style lang="css" scoped>
.date-link {
    text-decoration: none;
}
</style>
