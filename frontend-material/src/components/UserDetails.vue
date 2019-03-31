<template lang="html">
    <div class="UserDetails">
        {{ user }}
        <h1>Hello, {{ user.name }}!</h1>
        <v-card
          class="hide-overflow"
          color="primary lighten-1"
          dark
          flat
        >
          <v-toolbar
            card
            color="primary"
          >
            <v-icon>account_circle</v-icon>
            <v-toolbar-title class="font-weight-light">Your profile</v-toolbar-title>
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
              v-model='user.name'

            ></v-text-field>
            <v-autocomplete
              :disabled="!isEditing"
              :items="states"
              :filter="customFilter"
              color="white"
              item-text="name"
              label="Timezone"
            ></v-autocomplete>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="!isEditing"
              color="success"
              @click="save"
            >
              Save
            </v-btn>
          </v-card-actions>
          <v-snackbar
            v-model="hasSaved"
            :timeout="2000"
            absolute
            bottom
            left
          >
            Your profile has been updated
          </v-snackbar>
        </v-card>
    </div>
</template>

<script>
export default {
    data () {
       return {
         user: this.$store.getters.currentUser,
         hasSaved: false,
         isEditing: null,
         model: null,
         states: [
           { name: 'Florida', abbr: 'FL', id: 1 },
           { name: 'Georgia', abbr: 'GA', id: 2 },
           { name: 'Nebraska', abbr: 'NE', id: 3 },
           { name: 'California', abbr: 'CA', id: 4 },
           { name: 'New York', abbr: 'NY', id: 5 }
       ],
        timezones: [
            'Asia/Macau',
            'Asia/Novosibirsk',
            'Europe/Moscow',
            'America/Vancouver'
        ]
       }
     },

     methods: {
       customFilter (item, queryText, itemText) {
         const textOne = item.name.toLowerCase()
         const textTwo = item.abbr.toLowerCase()
         const searchText = queryText.toLowerCase()

         return textOne.indexOf(searchText) > -1 ||
           textTwo.indexOf(searchText) > -1
       },
       save () {
         this.isEditing = !this.isEditing
         this.hasSaved = true
       }
     }
}
</script>

<style lang="css" scoped>
</style>
