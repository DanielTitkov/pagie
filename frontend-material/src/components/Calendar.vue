<template>
    <div class="calendar">

        {{ selectedDate }}

        <v-expansion-panel expand flat color='primary' class='ma-4'>
          <v-expansion-panel-content>
            <template slot="header">Show calendar</template>
            <v-card flat>
              <v-card-text>
                  <v-date-picker
                      v-model="selectedDate"
                      full-width
                      landscape
                      class="ma-3"
                      reactive
                  ></v-date-picker>
              </v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selectedDate: null
        }
    }
}
</script>

<style scoped>
</style>
