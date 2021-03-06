<template lang="html">
    <div class="writer">
        <v-layout row wrap justify-center>
            <v-flex xs12 md10 lg8 xl6 @keydown.ctrl.83.prevent="saveText">
                <h4 class="grey--text title">
                    {{ dateslug | toReadableDate }}, {{ currentUser.timezone }}
                </h4>
                <div class="text-wrapper">
                    <v-textarea
                        @keyup="saveTextTimeout"
                        v-model="text"
                        :disabled="disabled"
                        :loading="disabled"
                        class="title my-3 font-weight-regular"
                        auto-grow
                        label="Write your words"
                        color="grey lighten-1"
                        row-height="50"
                    />
                </div>
            </v-flex>
        </v-layout>
        <v-layout row wrap justify-start>
            <v-flex xs0 md1 lg2 xl3></v-flex>
            <v-flex xs6 md2 lg2 xl2 class="grey--text"
                >{{ savedStatus }}
                <!-- <span v-if="savedTime">{{ savedTime | tsToDatetime }}</span> -->
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex xs6 md2 lg2 xl2 class="text-xs-right grey--text">
                {{ wordsCount }} words
            </v-flex>
            <v-flex xs0 md1 lg2 xl3></v-flex>
        </v-layout>
    </div>
</template>

<script>
import { countWords } from '@/helpers/text';
import { encryptUserData, decryptUserData } from '@/helpers/crypto';
import axios from 'axios';
import config from '@/config';

var moment = require('moment');

export default {
    props: {
        dateslug: {
            type: String,
            required: false,
            default: ''
        }
    },
    data() {
        return {
            savedStatus: null,
            // savedTime: null,
            saveTimeout: null,
            text: '',
            loading: false
        };
    },
    watch: {
        dateslug: function() {
            this.getText();
        }
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
        },
        currentUserKey() {
            return this.$store.getters.currentUserKey;
        },
        disabled() {
            if (this.dateslug == this.date && !this.loading) {
                return false;
            } else {
                return true;
            }
        }
    },
    created() {
        if (this.dateslug && this.dateslug.length == 8) {
            this.getText();
        }
    },
    methods: {
        getText: function() {
            this.loading = true;
            this.text = 'loading...';
            axios
                .get(config.API_URL + 'texts', {
                    params: {
                        dateslug: this.dateslug
                    },
                    headers: {
                        Authorization: `Bearer ${
                            this.$store.getters.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    if (response.data[0]) {
                        var encryptedText = response.data[0].text;
                        this.text = decryptUserData(
                            encryptedText,
                            this.currentUserKey
                        );
                    } else {
                        this.text = 'No text for this date';
                    }
                    this.loading = false;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        saveText: function(instance, reset = true) {
            if (reset) {
                instance = this;
            }
            instance.savedStatus = 'saving...';
            axios
                .post(
                    config.API_URL + 'texts',
                    {
                        text: encryptUserData(
                            instance.text,
                            instance.currentUserKey
                        ),
                        dateslug: instance.date,
                        words: instance.wordsCount
                    },
                    {
                        headers: {
                            Authorization: `Bearer ${
                                instance.currentUser.token
                            }`
                        }
                    }
                )
                .then(response => {
                    instance.savedStatus = `Saved ${countWords(
                        instance.text
                    )} words at ${moment().format('HH:mm')}`;
                    // instance.savedTime = response.data.updated * 1000; // Python timestamps are in seconds
                });
        },
        saveTextTimeout: function() {
            clearTimeout(this.saveTimeout); // clear timeout variable

            var self = this;
            this.saveTimeout = setTimeout(function() {
                self.saveText(self, false);
            }, 1000);
        }
    }
};
</script>

<style>
.writer .text-wrapper textarea {
    font-size: 20px;
    line-height: 1.5em;
    padding: 10px 0px;
}
</style>
