<template lang="html">
    <div class="writer">
        <v-layout row wrap justify-center>
            <v-flex xs12 md10 xl8>
                <h4 class="grey--text">
                    {{ date }}, {{ currentUser.timezone }}
                </h4>
                <v-textarea
                    @keyup="saveText"
                    v-model="text"
                    :disabled='disabled'
                    class="title font-weight-light pa-5"
                    auto-grow
                    label="Write your words"
                    append-icon="favorite"
                >
                </v-textarea>
                {{ savedStatus }}
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex xs0 md1 xl2></v-flex>
            <v-flex xs6 md5 xl4> {{ wordsCount }} words </v-flex>
        </v-layout>
    </div>
</template>

<script>
import { countWords } from '@/helpers/text';
import axios from 'axios';

export default {
    data() {
        return {
            text: '',
            savedStatus: 'not saved',
            saveTimeout: null,
            disabled: true
        };
    },
    computed: {
        wordsCount() {
            return countWords(this.text);
        },
        date() {
            return this.$store.getters.date;
        },
        currentUser() {
            return this.$store.getters.currentUser;
        }
    },
    mounted() {
        this.$store.dispatch('getDate');
    },
    methods: {
        saveText: function() {
            clearTimeout(this.saveTimeout); // clear timeout variable

            var self = this;
            this.saveTimeout = setTimeout(function() {
                axios
                    .post(
                        'http://127.0.0.1:5000/v1/texts', {
                            text: self.text,
                            dateslug: self.date
                        }, {
                            headers: {
                                Authorization: `Bearer ${
                                    self.currentUser.token
                                }`
                            }
                        }
                    )
                    .then(response => {
                        self.savedStatus = `Saved ${countWords(
                            self.text
                        )} words at ${response.data.updated}`;
                    });
            }, 2000);
        }
    }
};
</script>

<style scoped></style>
