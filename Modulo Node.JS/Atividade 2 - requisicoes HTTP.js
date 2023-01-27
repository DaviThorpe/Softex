const http = require('http');

const server = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.end('Olá, mundo!');
});

server.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});

//Aqui está um exemplo de um servidor HTTP básico que retorna uma mensagem de "Olá, mundo!" para todas as requisições
