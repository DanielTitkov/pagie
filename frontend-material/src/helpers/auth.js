import axios from 'axios';
import config from '@/config';

export function login(credentials) {
    return new Promise((res, rej) => {
        axios
            .post(config.API_URL + 'token', credentials)
            .then(response => {
                res(response.data);
            })
            .catch(err => {
                rej('Login failed');
            });
    });
}

export function getLocalUser() {
    const userStr = localStorage.getItem('user');

    if (!userStr) {
        return null;
    }

    return JSON.parse(userStr);
}

export function getLocalUserKey() {
    const userKey = localStorage.getItem('userKey');

    if (!userKey) {
        return null;
    }

    return userKey;
}

export function postUser(userData) {
    return new Promise((res, rej) => {
        axios
            .post(config.API_URL + 'users', userData)
            .then(response => {
                res(response.data);
            })
            .catch(err => {
                rej('Signup failed');
            });
    });
}

// export function postUser(userData) {
//     return axios.post(config.API_URL + 'users', userData);
// }
