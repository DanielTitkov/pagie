<template>
    <div class="about">
        <h1 class="grey--text">Profile</h1>
        <v-container class="my-5">
            <UserDetails />
        </v-container>
    </div>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    components: {
        UserDetails: () => import('@/components/UserDetails.vue'),
    },
};
</script>
