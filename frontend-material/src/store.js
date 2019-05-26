import { getLocalUser, getLocalUserKey } from '@/helpers/auth';
import axios from 'axios';
import config from '@/config';

const user = getLocalUser();
const userKey = getLocalUserKey();

export default {
    state: {
        currentUser: user,
        currentUserKey: userKey,
        isLoggedIn: !!user && !!userKey,
        loading: false,
        authError: null,
        date: null,
        darkTheme: false,
        datesData: []
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
        currentUserKey(state) {
            return state.currentUserKey;
        },
        authError(state) {
            return state.authError;
        },
        date(state) {
            return state.date;
        },
        datesData(state) {
            return state.datesData;
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
            state.currentUser = Object.assign({}, payload.response.user, {
                token: payload.response.access_token
            });
            localStorage.setItem('user', JSON.stringify(state.currentUser));
            localStorage.setItem('userKey', payload.decryptedUserKey);
            state.currentUserKey = payload.decryptedUserKey;
        },
        saveUserKey(state, payload) {
            // not really good??
            localStorage.setItem('userKey', payload);
        },
        loginFailed(state, payload) {
            state.loading = false;
            state.authError = payload.error;
        },
        logout(state) {
            localStorage.removeItem('user');
            localStorage.removeItem('userKey');
            state.isLoggedIn = false;
            state.currentUser = null;
            state.currentUserKey = null;
        },
        updateDate(state, payload) {
            state.date = payload;
        },
        updateDatesData(state, payload) {
            state.datesData = payload;
        },
        updateCurrentUser(state, payload) {
            state.currentUser = payload;
            localStorage.setItem('user', JSON.stringify(state.currentUser));
        }
    },
    actions: {
        login(context) {
            context.commit('login');
        },
        getDate(context) {
            axios
                .get(config.API_URL + 'date', {
                    headers: {
                        Authorization: `Bearer ${
                            context.state.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    context.commit('updateDate', response.data.dateslug);
                });
        },
        getDatesData(context) {
            axios
                .get(config.API_URL + 'dates', {
                    headers: {
                        Authorization: `Bearer ${
                            context.state.currentUser.token
                        }`
                    }
                })
                .then(response => {
                    context.commit('updateDatesData', response.data);
                });
        },
        updateUser({ commit, state }, payload) {
            return new Promise((resolve, reject) => {
                axios
                    .post(config.API_URL + 'users/' + payload.uid, payload, {
                        headers: {
                            Authorization: `Bearer ${state.currentUser.token}`
                        }
                    })
                    .then(response => {
                        commit(
                            'updateCurrentUser',
                            Object.assign({}, response.data, {
                                token: state.currentUser.token
                            })
                        );
                        resolve(response);
                    })
                    .catch(err => {
                        reject(err);
                    });
            });
        }
    }
};
