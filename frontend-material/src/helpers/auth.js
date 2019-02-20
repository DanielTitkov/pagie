import axios from 'axios';

export function login(credentials) {
    return new Promise((res, rej) => {
        axios
            .post('http://127.0.0.1:5000/v1/token', credentials)
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
