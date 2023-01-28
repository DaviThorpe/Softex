// Crie um código Node.JS usando a biblioteca Express. 
//Nele, você deve receber quatro tipos de requisições e responder cada uma com strings diferentes. 
//Por fim, explique como rodar o código.

const express = require('express');

const app = express();

app.get('/', (request, response) => {
  response.send('Recebi uma requisição GET');
});

app.post('/', (request, response) => {
  response.send('Recebi uma requisição POST');
});

app.put('/', (request, response) => {
  response.send('Recebi uma requisição PUT');
});

app.delete('/', (request, response) => {
  response.send('Recebi uma requisição DELETE');
});

app.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});

// Para rodar o código, deve-se usar o comando "node" seguido do nome do arquivo no terminal ou prompt de comando.