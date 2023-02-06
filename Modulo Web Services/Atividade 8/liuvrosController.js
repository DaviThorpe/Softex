
const livros = require('./dataBase');

exports.get = (req, res, next) => {
    res.status(200).send(livros);
};

exports.post = (req, res, next) => {
    var livro = req.body;
    livros.push(livro);
    res.status(201).send(req.body);
};

exports.put = (req, res, next) => {
    livros[req.params.index] = req.body;
    res.status(200).send(livros[req.params.index]); 
};

exports.delete = (req, res, next) => {
    var index = req.params.index;
    livros.splice(index, 1);
    res.status(200).send('Recurso deletado com sucesso.');
};
