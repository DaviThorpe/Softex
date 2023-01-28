//Usando o Express, crie um código Node.JS, que deve receber requisições HTTP GET e POST. 
//Depois, coloque o servidor para rodar na porta 8080.

const express = require('express');

const app = express();

app.get('/get', (request, response) => {
  response.send('Recebi uma requisição GET');
});

app.post('/post', (request, response) => {
  response.send('Recebi uma requisição POST');
});

app.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});
