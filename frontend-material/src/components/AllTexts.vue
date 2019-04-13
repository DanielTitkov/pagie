<template>
    <div class="AllTexts">
        <h3>{{ status }}</h3>
        {{ texts }}
    </div>
</template>

<script>
import axios from 'axios';
import config from "@/config";

export default {
    data() {
        return {
            texts: [],
            loading: true,
            status: ''
        }
    },
    methods: {
        fetchTexts() {
            this.loading = true;
            this.status = 'loading...';
            axios
                .get(config.API_URL + 'texts', {
                    headers: {
                        Authorization: `Bearer ${
                            this.$store.getters.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    this.texts = response.data;
                    this.loading = false;
                    this.status = 'updated';
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    created() {
        this.fetchTexts();
    }
}
</script>

<style lang="css" scoped>
</style>
