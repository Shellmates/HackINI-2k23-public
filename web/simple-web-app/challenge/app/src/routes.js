const express = require('express');
const router = express.Router();
const path = require('path');
const config = require('./config');
const { users } = require('./database');
const { a,b, login, signup } = require('./graphql');

const viewsPath = 'app/views/';

// middlewares 

// check token
function checkTokenMiddleware(req, resp, next) {
    let token = req.cookies[config.COOKIE_SESSION_NAME];
    req.user = token? users.find(user => user.token == token) : null;
    next();
}
// check if authenticated to tredirect to /profile 
function reidrectionMiddleware(req, resp, next) {
    if (req.user)
        resp.redirect('/profile');
    else if (req.url === '/profile') 
        resp.redirect('/login');
    else
        next();
}
// check authentication to access /profile
function profileAuthMiddleware(req, resp, next) {
    if (req.user)
        next();
    else 
        resp.redirect('/login');
}

router.use(checkTokenMiddleware);
router.use('(/register|/login)', reidrectionMiddleware);
router.use('(/profile|/logout)', profileAuthMiddleware);


// routes

// GET
router.get('/', (req, resp) => {
    resp.redirect('/login');
});

router.get('/register', (req, resp) => {
    resp.sendFile(path.resolve(viewsPath + 'register.html'));
});

router.get('/login', (req, resp) => {
    resp.sendFile(path.resolve(viewsPath + 'login.html'));
});

router.get('/profile', (req, resp) => {
    if (req.user.role == 'ADMIN')
        resp.sendFile(path.resolve(viewsPath + 'admin.html'));
    else
        resp.sendFile(path.resolve(viewsPath + 'profile.html'));
});

// POST
router.post('/register', (req, resp) => {
    let data = req.body;
    let json = { success: false, message: ""};
    
    try {
        json.success = Boolean(signup(data.username, data.password, data.email));
        json.message = json.success ? "Registered successsfully" : "An error occured"
    } catch (error) {
        json.message = error.message;
    }
    
    resp.json(json);
});

router.post('/login', (req, resp) => {
    let data = req.body;
    let result = login(data.username, data.password);
    let success = result.success;
    let json = { 
        success: success, 
        message: success ? "Logged successfully" : "Incorrect username or password",
    };

    if (success) 
        resp.cookie( config.COOKIE_SESSION_NAME, result.token, { httpOnly: true } )
    
    resp.json(json);
});

router.post('/logout', (req, resp) => {
    req.user.token = null;
    resp.redirect('/');
});


module.exports = router;
