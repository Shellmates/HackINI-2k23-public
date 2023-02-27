const config = require('./config');
const { users } = require('./database');
const { User, hash } = require('./models');
const { GraphQLError } = require("graphql");
const { ApolloServerErrorCode } = require('@apollo/server/errors');
const fs = require("fs");
const crypto = require("crypto");

function signup(username, password, email, role) {
    if (users.length == config.MAX_USERS) { users = []; }
    if (users.find(user => user.username === username)) {
        throw new GraphQLError("User already exists", {
            extensions: { code: "USER_EXISTS" },
        });
    }
    if (!(username && password)) {
        throw new GraphQLError("Bas user input", {
            extensions: { code: ApolloServerErrorCode.BAD_USER_INPUT },
        });
    }
    return users.push(new User(username, password, email, role));
}

function login(username, password) {
    let user = users.find( u => u.username === username && hash(password) === u.password );
    let logged =  Boolean(user);
    let token = logged? crypto.randomBytes(config.TOKEN_LENGTH).toString('hex') : null;
    if (logged) user.token = token;
    return {
        success: logged,
        token: token,
    }
}

// graphql 

const typeDefs = fs.readFileSync('./app/schema.graphql', 'utf8');

const queriesResolvers = {
    user: ( parent, args, context ) => { 
        return users.find(user => user.token === context.token); 
    },
};

const mutationsResolvers = {
    addUser: (parent, {username, password, email, role}, context ) => signup(username, password, email, role),
    authUser: (parent, {username, password}, context ) => login(username, password),
};

const resolvers = {
    Query: queriesResolvers,
    Mutation: mutationsResolvers,
};

exports.typeDefs = typeDefs;
exports.resolvers = resolvers;
exports.login = login;
exports.signup = signup;