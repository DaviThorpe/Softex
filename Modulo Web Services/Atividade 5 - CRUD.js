/* Demonstre como fazer as quatro operações de CRUD e suas rotas para obter o 
recurso de um livro que está no estoque de uma livraria. 
Um livro possui informações como nome, autor e ISBN.*/

const express = require('express');
const app = express();
app.use(express.json());

app.get('/livros', (req, res) => {
    const livros = [
        {
            "id": 1,
            "nome": "One Piece",
            "autor": "Eiichiro Oda",
            "ISBN": "000-0-00-000000-0"
        },
        {
            "id": 2,
            "nome": "Hunter Hunter",
            "autor": "Yoshihiro Togashi",
            "IBSN": "000-0-00-000000-1"
        },
        {
            "id": 3,
            "nome": "Shingeki no Kyojin",
            "autor": "Hajime Isayama",
            "IBSN": "000-0-00-000000-3"
        }
    ];
    res.json(livros);
});

app.get('/livros/:id', (req, res) => {
    const idLivro = req.params;
    res.json(idLivro);
});

app.post('/livros', (req, res) => {
    res.json(req.body);
});

app.put('/livros/:id', (req, res) => {
    const idLivro = req.params;
    res.json(req.body);
});

app.delete('/livros/:id', (req, res) => {
    const idLivro = req.params;
    res.json(idLivro);
});

app.listen(8080, () => {
    console.log('Servidor rodando!');
});
