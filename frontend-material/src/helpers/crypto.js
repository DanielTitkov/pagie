const uuidv4 = require('uuid/v4');
var crypto = require('crypto');

export function createUserKey() {
    return uuidv4(); // change the algorithm later;
}

export function hashUserPassword(password, hashFunc='sha256') {
    return crypto
        .createHash(hashFunc)
        .update(password)
        .digest('hex');
}

export function encryptUserData(data, key) {
    var cipher = crypto.createCipher('aes-256-ctr', key);
    var crypted = cipher.update(data, 'utf8', 'hex');
    crypted += cipher.final('hex');
    return crypted;
}

export function decryptUserData(ecryptedData, key) {
    var decipher = crypto.createDecipher('aes-256-ctr', key);
    var decrypted = decipher.update(ecryptedData, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
}
