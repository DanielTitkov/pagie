<template>
    <div class="login">
        <v-layout row wrap justify-center>
            <v-flex xs12 sm9 md7 lg5>
                <v-card flat>
                    <v-card-title>
                        <h2 class="grey--text">Login to Pagie</h2>
                    </v-card-title>
                    <v-card-text>
                        <v-alert
                            class="mx-3 mb-3"
                            v-if="authError"
                            dismissible
                            value="true"
                            type="error"
                        >
                            {{ authError }}
                        </v-alert>
                        <v-form class="px-3">
                            <v-text-field
                                label="Email"
                                v-model="form.email"
                            ></v-text-field>
                            <v-text-field
                                label="Password"
                                v-model="rawPassword"
                                :type="showPassword ? 'text' : 'password'"
                                :rules="[rules.required]"
                                :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                                @click:append="showPassword = !showPassword"
                                counter
                            ></v-text-field>
                            <v-btn
                                depressed
                                color="primary"
                                @click="authenticate"
                                >Sign in</v-btn
                            >
                            <router-link to="register"
                                >Or create account</router-link
                            >
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import { login } from '@/helpers/auth';
import { decryptUserData, hashUserPassword } from '@/helpers/crypto';

export default {
    data() {
        return {
            form: {
                email: '',
                password: ''
            },
            rawPassword: '',
            userPasswordHash: '',
            error: null,
            showPassword: false,
            rules: {
              required: value => !!value || 'Required.'
            }
        };
    },
    methods: {
        authenticate() {
            this.$store.dispatch('login');
            this.userPasswordHash = hashUserPassword(this.$data.rawPassword);
            this.form.password = hashUserPassword(this.rawPassword, 'sha512');
            login(this.$data.form)
                .then(response => {
                    var decryptedUserKey = decryptUserData(response.user.userKey, this.userPasswordHash);
                    const loginData = {
                        response: response,
                        decryptedUserKey: decryptedUserKey
                    }
                    this.$store.commit('loginSuccess', loginData);
                    this.$router.push({ path: '/' });
                })
                .catch(error => {
                    this.$store.commit('loginFailed', { error });
                });
        }
    },
    computed: {
        authError() {
            return this.$store.getters.authError;
        }
    }
};
</script>

<style scoped></style>
