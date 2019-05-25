<template>
    <nav>
        <v-toolbar app flat>
            <v-toolbar-side-icon
                v-if="currentUser"
                class="grey--text"
                @click="drawer = !drawer"
            ></v-toolbar-side-icon>
            <v-toolbar-title class="grey--text">
                <span class="font-weight-light pagie-title">Pagie</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn router to="/intro" flat color="grey">
                <span>Intro</span>
            </v-btn>
            <div v-if="currentUser">
                <!-- <h2>{{ currentUser.name }}</h2> -->
                <v-btn flat mdAndUp color="grey" @click="logout">
                    <span class="hidden-sm-and-down">Log out</span>
                    <v-icon right>exit_to_app</v-icon>
                </v-btn>
            </div>
            <div v-else>
                <v-btn router to="/login" flat color="grey">
                    <span>Sign in</span>
                </v-btn>
                <v-btn router to="/register" flat color="grey">
                    <span>Register</span>
                </v-btn>
            </div>
        </v-toolbar>

        <v-navigation-drawer
            v-if="currentUser"
            v-model="drawer"
            app
            class="primary"
        >
            <v-list>
                <!-- Hide drawer -->
                <v-list-tile @click="drawer = !drawer">
                    <v-list-tile-action class="white--text">
                        <v-icon>
                            arrow_back
                        </v-icon>
                    </v-list-tile-action>
                </v-list-tile>
                <!-- Menu -->
                <v-list-tile
                    v-for="link in links"
                    :key="link.text"
                    router
                    :to="link.route"
                >
                    <v-list-tile-action class="white--text">
                        <v-icon>
                            {{ link.icon }}
                        </v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content class="white--text">
                        <v-list-tile-title>
                            {{ link.text }}
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            drawer: false,
            links: [
                { icon: 'favorite', text: 'Write!', route: '/' },
                { icon: 'calendar_today', text: 'History', route: '/history' },
                { icon: 'local_florist', text: 'About', route: '/about' },
                { icon: 'face', text: 'Profile', route: '/profile' },
                {
                    icon: 'format_list_bulleted',
                    text: 'Programs',
                    route: '/programs'
                },
                { icon: 'email', text: 'Contacts', route: '/contact' }
            ]
        };
    },
    methods: {
        logout() {
            this.$store.commit('logout');
            this.$router.push('/login');
        }
    },
    computed: {
        currentUser() {
            return this.$store.getters.currentUser;
        }
    }
};
</script>

<style></style>
