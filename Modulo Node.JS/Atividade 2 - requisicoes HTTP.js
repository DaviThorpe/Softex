//Sem usar bibliotecas, crie um projeto simples em Node.js que seja capaz de responder requisições HTTP.
//Explique como rodar e testar.

const http = require('http');

const server = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.end('Olá, mundo!');
});

server.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});

//Aqui está um exemplo de um servidor HTTP básico que retorna uma mensagem de "Olá, mundo!" para todas as requisições

// Para rodar o código abra o terminal ou o prompt de comando e navegue até a pasta do seu projeto usando o comando cd.
//Após isso basta digitar o comando "node" seguido do nome do arquivo que deseja executar.