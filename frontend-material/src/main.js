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

Vue.filter('toReadableDate', function(value) {
    try {
        var year = value.slice(0, 4);
        var month = value.slice(4, 6);
        var day = value.slice(6, 8);
        return day + '.' + month + '.' + year;
    } catch {
        return 'loading...';
    }
});

// var moment = require('moment');
//
// Vue.filter('tsToDatetime', function(ts) {
//     var date = new Date(ts);
//     // return date.toISOString();
//     return moment().format('HH:mm');
// });

initialize(store, router);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
