<template lang="html">
    <div class="register">
        <v-layout row wrap justify-center>
            <v-flex xs12 sm9 md7 lg5>
                <v-card flat>
                    <v-card-title>
                        <h2 class="grey--text">Create account</h2>
                    </v-card-title>
                    <v-card-text>
                        <v-alert
                            class="mx-3 mb-3"
                            v-if="error"
                            dismissible
                            value="true"
                            type="error"
                        >
                            {{ error }}
                        </v-alert>
                        <v-form class="px-3">
                            <v-text-field
                                label="Name"
                                v-model="form.name"
                            ></v-text-field>
                            <v-text-field
                                label="Email"
                                v-model="form.email"
                            ></v-text-field>
                            <v-text-field
                                label="Password"
                                v-model="form.password"
                            ></v-text-field>
                            <v-text-field
                                label="Repeat password"
                                v-model="passwordRepeat"
                            ></v-text-field>
                            <v-btn
                                depressed
                                color="primary"
                                @click="createUser"
                                :disabled="passwordError"
                                >Sign up</v-btn
                            >
                            <router-link to="login">Or log in</router-link>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import { postUser } from '@/helpers/auth';
import {
    createUserKey,
    hashUserPassword,
    encryptUserData,
    decryptUserData
} from '@/helpers/crypto';

export default {
    data() {
        return {
            form: {
                name: '',
                email: '',
                password: '',
                userKey: '',
            },
            userPasswordHash: '',
            passwordRepeat: '',
            error: null
        };
    },
    computed: {
        passwordError() {
            return this.form.password != this.passwordRepeat;
        }
    },
    methods: {
        createUser() {
            this.userPasswordHash = hashUserPassword(this.form.password);
            this.form.userKey = encryptUserData(
                createUserKey(),
                this.userPasswordHash
            );
            postUser(this.$data.form)
                .then(response => {
                    this.$router.push({ path: '/login' });
                })
                .catch(err => {
                    this.error = err;
                    console.log(err);
                });
        }
    }
};
</script>

<style lang="css" scoped></style>
