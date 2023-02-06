const express = require('express')
const router = express.Router();

router 
    .get("/jogos", (req, res) => {
        //implementação de execução de busca
        console.log("busca")
    })
    .get("/jogos/:id", (req, res) => {
        // implementaçãi de execução de busca de único item
        console.log("busca específica") 
    })
    .post("/jogos", (req, res) => {
        //implementação de execução de cadastro
        console.log("cadastro")
    })
    .put("/jogos/:id", (req, res) => {
        //implementação de execução de atualização
        console.log("update")
    })
    .delete("/jogos/:id", (req, res) => {
        //implementação de execução delete
        console.log('delete')
    })

module.exports = router;
