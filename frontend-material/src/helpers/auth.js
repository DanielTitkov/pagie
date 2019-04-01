import axios from 'axios';

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
