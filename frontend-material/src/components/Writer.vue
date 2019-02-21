<template lang="html">
    <div class="writer">
        <v-layout row wrap justify-center>
            <v-flex xs12 md10 xl8>
                <h4 class="grey--text">
                    {{ date }}, {{ currentUser.timezone }}
                </h4>
                <v-textarea
                    @keyup="saveText"
                    v-model="todaysText"
                    :disabled="disabled"
                    :loading="disabled"
                    class="my-3"
                    auto-grow
                    label="Write your words"
                    append-icon="favorite"
                    row-height="50"
                >
                </v-textarea>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex xs0 md1 xl2></v-flex>
            <v-flex xs6 md2 xl2>{{ savedStatus }}</v-flex>
            <v-spacer></v-spacer>
            <v-flex xs6 md2 xl2 class="text-xs-right">
                {{ wordsCount }} words
            </v-flex>
            <v-flex xs0 md1 xl2></v-flex>
        </v-layout>
    </div>
</template>

<script>
import { countWords } from '@/helpers/text';
import axios from 'axios';

export default {
    data() {
        return {
            savedStatus: 'not saved',
            saveTimeout: null
        };
    },
    computed: {
        wordsCount() {
            return countWords(this.todaysText);
        },
        date() {
            return this.$store.getters.date;
        },
        currentUser() {
            return this.$store.getters.currentUser;
        },
        disabled() {
            return false;
            // this.$store.getters.todaysText;
        },
        todaysText: {
            get() {
                return this.$store.getters.todaysText;
            },
            set(value) {
                this.$store.commit('updateTodaysText', value);
            }
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
                        'http://127.0.0.1:5000/v1/texts',
                        {
                            text: self.todaysText,
                            dateslug: self.date
                        },
                        {
                            headers: {
                                Authorization: `Bearer ${
                                    self.currentUser.token
                                }`
                            }
                        }
                    )
                    .then(response => {
                        self.savedStatus = `Saved ${countWords(
                            self.todaysText
                        )} words at ${response.data.updated}`;
                    });
            }, 2000);
        }
    }
};
</script>

<style scoped>
.writer textarea {
    border: 1px solid blue;
    padding: 10px;
    line-height: 2;
    color: red;
}
</style>
