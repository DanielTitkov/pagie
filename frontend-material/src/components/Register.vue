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
                                :rules="[rules.required]"
                                v-model="form.name"
                            ></v-text-field>
                            <v-text-field
                                label="Email"
                                :rules="[rules.required]"
                                v-model="form.email"
                            ></v-text-field>
                            <p>
                                Select a good password and remember it well. It
                                will be used to encrypt your texts so that even
                                we won't be able to access them. If you forget
                                the password, it will be impossible to decrypt
                                your texts.
                            </p>
                            <v-text-field
                                label="Password"
                                v-model="rawPassword"
                                :type="showPassword ? 'text' : 'password'"
                                :rules="[rules.required, rules.min]"
                                :append-icon="
                                    showPassword
                                        ? 'visibility'
                                        : 'visibility_off'
                                "
                                @click:append="showPassword = !showPassword"
                                counter
                            ></v-text-field>
                            <v-text-field
                                label="Repeat password"
                                v-model="passwordRepeat"
                                :type="showPassword ? 'text' : 'password'"
                                :rules="[rules.required, rules.min]"
                                :append-icon="
                                    showPassword
                                        ? 'visibility'
                                        : 'visibility_off'
                                "
                                @click:append="showPassword = !showPassword"
                                counter
                            ></v-text-field>
                            <v-text-field
                                label="Invite code"
                                v-model="form.inviteCode"
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
    encryptUserData
} from '@/helpers/crypto';

export default {
    data() {
        return {
            form: {
                name: '',
                email: '',
                password: '',
                userKey: '',
                inviteCode: ''
            },
            rawPassword: '',
            userPasswordHash: '',
            passwordRepeat: '',
            showPassword: false,
            error: null,
            rules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 3 || 'Min 3 characters'
            }
        };
    },
    computed: {
        passwordError() {
            return this.rawPassword != this.passwordRepeat;
        }
    },
    methods: {
        createUser() {
            this.userPasswordHash = hashUserPassword(this.rawPassword);
            this.form.password = hashUserPassword(this.rawPassword, 'sha512'); // using sha512 of user password for auth
            this.form.userKey = encryptUserData(
                createUserKey(),
                this.userPasswordHash
            );
            postUser(this.$data.form)
                .then(response => {
                    this.$router.push({ path: '/login' });
                })
                .catch(err => {
                    this.error = 'Signup failed';
                });
        }
    }
};
</script>

<style lang="css" scoped></style>
