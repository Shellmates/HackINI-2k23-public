const crypto = require("crypto");
const config = require('./config');

function hash(password) {
    return crypto.pbkdf2Sync(password, '', 50, config.HASH_LENGTH, 'sha512').toString('hex'); 
}

const Roles = ['ADMIN','USER','MODERATOR'];

class User {
    constructor(name, pass, mail, role='USER', token=null) {
        this.username = name;
        this.password = hash(pass);
        this.email = mail;
        //this.isAdmin = admin;
        this.role = Roles.includes(role) ? role : 'USER';
        this.token = token;
    }
}

exports.User = User;
exports.hash = hash;
