const app = require('./app');
const debug = require('debug')('balta:server');
const http = require('http');

const port = normalizePort(process.env.PORT || '8080');
app.set('port', port);

const server = http.createServer(app);

server.listen(port);
server.on('error', onError);
server.on('listening', onListening)

console.log(`Server rodando na porta ${port}`);

function normalizePort(val){
    const port = parseInt(val, 10);
    if(isNaN(port)){
        return val;
    }
    if(port >= 0){
        return port;
    }
    return false;
}

function onError(error){
    if (error.sycall !== 'listen'){
        throw error;
    }
    const bind = typeof port === 'string' ?
        'pipe' + port :
        'port' + port;
    switch (error.code){
        case 'EACCES' :
            console.error(`${bind} requires elevated privileges`)
            process.exit(1);
            break;
        case 'EADDRINUSE':
            console.error(`${bind} is already in use`);
            process.exit(1);
        default:
            throw error;
    }
}

function onListening(){
    const addr = server.address();
    const bind = typeof addr === 'string'
        ? 'pipe' + addr
        : 'port + addr.port';
    debug(`Listening on ${bind}`)
}
