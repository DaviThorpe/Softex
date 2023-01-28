//Crie um pequeno servidor web que contenha várias rotas.
//Em cada rota, você deverá fazer o controle do fluxo de requisições de maneira estática ou dinâmica, 
//alterne entre essas formas usando placeholders e query.

const express = require('express');

const app = express();

// Rota estática que responde a requisições GET na rota raiz
app.get('/', (request, response) => {
  response.send('Recebi uma requisição GET');
});

// Rota dinâmica que usa um placeholder para aceitar um ID de usuário
app.get('/usuarios/:id', (request, response) => {
  const id = request.params.id;
  response.send(`Recebi uma requisição GET para o usuário com ID ${id}`);
});

// Rota que usa o objeto request.query para ler os parâmetros da query string
app.get('/produtos', (request, response) => {
  const usuario = request.query.usuario;
  const id = request.query.id;
  response.send(`Recebi uma requisição GET para o produto com usario ${usuario} e seu id ${id}`);
});

app.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});