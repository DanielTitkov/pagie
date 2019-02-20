import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import 'vuetify/src/stylus/app.styl';

Vue.use(Vuetify, {
    iconfont: 'md',
    theme: {
        primary: '#673ab7',
        secondary: '#8bc34a',
        accent: '#2196f3',
        error: '#e91e63',
        warning: '#ff9800',
        info: '#607d8b',
        success: '#4caf50'
    }
});
