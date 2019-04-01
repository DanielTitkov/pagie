<template lang="html">
    <div class="UserDetails">
        <v-card class="hide-overflow" color="primary lighten-1" dark flat>
            <v-toolbar card color="primary">
                <v-icon>account_circle</v-icon>
                <v-toolbar-title class="font-weight-light"
                    >Your profile</v-toolbar-title
                >
                <v-spacer></v-spacer>
                <v-btn
                    color="primary darken-3"
                    fab
                    small
                    @click="isEditing = !isEditing"
                >
                    <v-icon v-if="isEditing">close</v-icon>
                    <v-icon v-else>edit</v-icon>
                </v-btn>
            </v-toolbar>
            <v-card-text>
                <v-text-field
                    :disabled="!isEditing"
                    color="white"
                    label="Name"
                    v-model="user.name"
                ></v-text-field>
                <v-autocomplete
                    :disabled="!isEditing"
                    :items="timezones"
                    color="white"
                    item-text="name"
                    label="Timezone"
                    v-model="user.timezone"
                ></v-autocomplete>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled="!isEditing" color="success" @click="save">
                    Save
                </v-btn>
            </v-card-actions>
            <v-snackbar v-model="hasSaved" :timeout="2000" absolute bottom left>
                Your profile has been updated
            </v-snackbar>
        </v-card>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: this.$store.getters.currentUser,
            payload: {},
            localUser: JSON.parse(localStorage.getItem('user')),
            hasSaved: false,
            isEditing: null,
            model: null,
            timezones: [
                'Asia/Macau',
                'Asia/Novosibirsk',
                'Europe/Moscow',
                'America/Vancouver'
            ]
        };
    },
    methods: {
        save() {
            this.isEditing = !this.isEditing;
            this.$store
                .dispatch('updateUser', this.user)
                .then(response => {
                    this.hasSaved = true;
                    this.payload = this.user;
                })
                .catch(err => {
                    console.log(err);
                });
        }
    }
};
</script>

<style lang="css" scoped></style>
