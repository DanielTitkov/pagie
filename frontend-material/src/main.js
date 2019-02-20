import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import Vuex from 'vuex';
import StoreData from './store';
import { initialize } from '@/helpers/requests';

Vue.config.productionTip = false;

Vue.use(Vuex);

const store = new Vuex.Store(StoreData);

initialize(store, router);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
