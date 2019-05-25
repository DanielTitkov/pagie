<template>
    <div class="Intro">
        <v-container class="my-5">
            <v-layout row wrap justify-center mb-5>
                <v-flex xs12 md9 lg7>
                    <h1 class="display-4 pagie-title text-xs-center grey--text text--darken-2">Pagie</h1>
                    <p class='headline pt-5 pb-3'>Pagie is an app for expressive writing. Expressive writing is good for your mood,
                    eases stress and helps to solve everyday problems. It's a <a target="_blank" href="https://www.apa.org/monitor/jun02/writing">sciency thing</a>,
                    by the way.</p>
                    <p class='headline pb-4 pt-2'>
                    <b>Instructions:</b> Write whatever comes into your head. If nothing does write about it.
                    </p>
                    <h2 class="display-3 pagie-title text-xs-center grey--text text--darken-2">Write for happiness</h2>
                </v-flex>
            </v-layout>

            <v-layout row wrap justify-center my-5>
                <v-flex xs12 md9 lg7>
                    <h3 class="display-1 secondary--text" my-4>Easy to use</h3>
                    <v-layout row wrap justify-center>
                        <v-flex xs11 md7 my-3 class='headline'>
                            Just open and write. Pagie will save and keep your work.
                        </v-flex>
                        <v-flex xs1 md5 my-3 px-5>
                            <v-img :src="require('@/assets/icons8-edit-512.png')" alt="Pencil"></v-img>
                        </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>

            <v-layout row wrap justify-center my-5>
                <v-flex xs12 md9 lg7>
                    <h3 class="display-1 secondary--text" >Private</h3>
                    <v-layout row wrap justify-center>
                        <v-flex xs1 md5 my-3 px-5>
                            <v-img :src="require('@/assets/icons8-bookmark-512.png')" alt="Book"></v-img>
                        </v-flex>
                        <v-flex xs11 md7 my-3 class='headline'>
                            Everything you write here is just for you. No sharing, no social functions, no Facebook integration.
                            Pagie is your private space.
                        </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>

            <v-layout row wrap justify-center my-5>
                <v-flex xs12 md9 lg7>
                    <h3 class="display-1 secondary--text">Secure</h3>
                    <v-layout row wrap justify-center>
                    <v-flex xs11 md7 my-3 class='headline'>
                        Texts are being enciphered on your side with the password you provide.
                        This password is never sent to the server (hash is used for authentication),
                        so it is impossible for us or any third party to dechipher and read them.
                    </v-flex>
                    <v-flex xs1 md5 my-3 px-5 justify-center>
                        <v-img :src="require('@/assets/icons8-lock-512.png')" alt="Lock"></v-img>
                    </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>

            <v-layout row wrap justify-center my-5>
                <v-flex xs12 md9 lg7>
                    <h3 class="display-1 secondary--text">Developing!</h3>
                    <v-layout row wrap justify-center>
                    <v-flex xs12 my-3 class='headline'>
                        <p><b>Pagie now in beta.</b> There can be some bugs. We are sorry for that.
                        Also, only basic functionality is supported as yet.</p>
                        Features to be added soon:
                        <ul class='mt-1'>
                            <li>Writing timer</li>
                            <li>Personal writing goals</li>
                        </ul>
                    </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>

        </v-container>
    </div>
</template>
