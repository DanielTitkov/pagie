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
                                v-model="form.password"
                            ></v-text-field>
                            <v-btn
                                depressed
                                color="primary"
                                @click="authenticate"
                                >Sign in</v-btn
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

export default {
    data() {
        return {
            form: {
                email: '',
                password: ''
            },
            error: null
        };
    },
    methods: {
        authenticate() {
            this.$store.dispatch('login');
            login(this.$data.form)
                .then(response => {
                    this.$store.commit('loginSuccess', response);
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
