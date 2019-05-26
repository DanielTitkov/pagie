import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'vuetify/src/stylus/app.styl';

Vue.use(Vuetify, {
    iconfont: 'md',
    theme: {
        primary: '#3f51b5',
        secondary: '#00c853',
        accent: '#002984',
        error: '#e91e63',
        warning: '#ff9800',
        info: '#607d8b',
        success: '#4caf50'
    }
});

// Vue.use(Vuetify, {
//     iconfont: 'md',
//     theme: {
//         primary: '#673ab7',
//         secondary: '#8bc34a',
//         accent: '#2196f3',
//         error: '#e91e63',
//         warning: '#ff9800',
//         info: '#607d8b',
//         success: '#4caf50'
//     }
// });
