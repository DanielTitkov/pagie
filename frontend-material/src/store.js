import { getLocalUser } from '@/helpers/auth';
import axios from 'axios';

const user = getLocalUser();

export default {
    state: {
        currentUser: user,
        isLoggedIn: !!user,
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
        },
        getDatesData(context) {
            axios
                .get('http://127.0.0.1:5000/v1/dates', {
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
                    .post(
                        'http://127.0.0.1:5000/v1/users/' + payload.uid,
                        payload,
                        {
                            headers: {
                                Authorization: `Bearer ${
                                    state.currentUser.token
                                }`
                            }
                        }
                    )
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
                        console.log(err);
                        reject(err);
                    });
            });
        }
    }
};
