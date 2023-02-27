const { ApolloServer } = require("@apollo/server");
const { expressMiddleware } = require( "@apollo/server/express4");
const cors = require("cors");
const { json } = require("body-parser");
const express = require("express");
const cookieParser = require("cookie-parser");
const { ApolloServerPluginLandingPageDisabled } = require('@apollo/server/plugin/disabled'); 
const { GraphQLError } = require("graphql");
const { ApolloServerErrorCode } = require('@apollo/server/errors');
const config = require('./config');
const router = require('./routes');
const { typeDefs, resolvers } = require('./graphql');

const app = express();

app.use(express.json());
app.use(cookieParser());
app.use('/static', express.static('app/public'));
app.use(router);


async function start() {
    const server = new ApolloServer({
        typeDefs,
        resolvers,
        introspection: true,
        includeStacktraceInErrorResponses: false,
        plugins: [ApolloServerPluginLandingPageDisabled()],
    });

    await server.start();

    app.use('/graphql', cors(), json(), expressMiddleware(server,
        {
            context: async ({req, res}) => {
                if (!req.user) {
                    throw new GraphQLError('not authenticated', {
                        extensions: { code: ApolloServerErrorCode.GRAPHQL_VALIDATION_FAILED },
                    });
                }
                return { token: req.user?.token };
            },
        },
        ));

    app.listen(config.PORT, () => {
        console.log(`server listening on port ${config.PORT}`);
    });
}

start();