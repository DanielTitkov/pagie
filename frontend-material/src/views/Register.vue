<template>
    <div class="register">
        <v-container class="my-5">
            <Register />
        </v-container>
    </div>
</template>

<script>
export default {
    components: {
        Register: () => import('@/components/Register.vue')
    }
};
</script>

<style scoped></style>
