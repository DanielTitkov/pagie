import { getLocalUser } from '@/helpers/auth';
import axios from 'axios';

const user = getLocalUser();

export default {
    state: {
        currentUser: user,
        isLoggedIn: !!user,
        loading: false,
        authError: null,
        date: null
    },
    getters: {
        isLoading(state) {
            return state.loading;
        },
        isLoggedIn(state) {
            return state.isLoggedIn;
        },
        currentUser(state) {
            return state.currentUser;
        },
        authError(state) {
            return state.authError;
        },
        date(state) {
            return state.date;
        }
    },
    mutations: {
        login(state) {
            state.loading = true;
            state.authError = null;
        },
        loginSuccess(state, payload) {
            state.authError = null;
            state.isLoggedIn = true;
            state.loading = false;
            state.currentUser = Object.assign({}, payload.user, {
                token: payload.access_token
            });
            localStorage.setItem('user', JSON.stringify(state.currentUser));
        },
        loginFailed(state, payload) {
            state.loading = false;
            state.authError = payload.error;
        },
        logout(state) {
            localStorage.removeItem('user');
            state.isLoggedIn = false;
            state.currentUser = null;
        },
        updateDate(state, payload) {
            state.date = payload;
        }
    },
    actions: {
        login(context) {
            context.commit('login');
        },
        getDate(context) {
            axios
                .get('http://127.0.0.1:5000/v1/date', {
                    headers: {
                        Authorization: `Bearer ${
                            context.state.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    context.commit('updateDate', response.data.dateslug);
                });
        }
    }
};
