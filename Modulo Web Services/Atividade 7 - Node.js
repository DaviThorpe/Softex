/*
Utilizando o Node.JS e a biblioteca Express, crie um projeto inicial que tenha uma página com o texto “Hello World”.
*/

const express = require('express');
const app = express();
const porta = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(porta, () => {
  console.log(`Example app listening on port ${porta}`)
})
