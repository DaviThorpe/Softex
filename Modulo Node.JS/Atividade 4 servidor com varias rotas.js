const express = require('express');

const app = express();

// Rota estática que responde a requisições GET na rota raiz
app.get('/', (request, response) => {
  response.send('Recebi uma requisição GET na rota raiz');
});

// Rota dinâmica que usa um placeholder para aceitar um ID de usuário
app.get('/usuarios/:id', (request, response) => {
  const id = request.params.id;
  response.send(`Recebi uma requisição GET para o usuário com ID ${id}`);
});

// Rota que usa o objeto request.query para ler os parâmetros da query string
app.get('/produtos', (request, response) => {
  const nome = request.query.nome;
  const preco = request.query.preco;
  response.send(`Recebi uma requisição GET para o produto com nome ${nome} e preço ${preco}`);
});

app.listen(8080, () => {
  console.log('Servidor iniciado na porta 8080');
});