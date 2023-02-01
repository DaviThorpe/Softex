/* Faça um projeto explicando como funcionam os métodos HTTP com exemplos de requisições, 
sua utilização e em qual momento cada um dos métodos devem ser utilizados. 
Além disso, descreva o que é WSDL, seu significado e sua função.*/

const express = require("express")
const app = express()

app.get("/", (req, res) => {
    res.send(`Esta é uma requisição GET.`) // O método GET solicita a representação de um recurso específico. Requisições utilizando o método GET devem retornar apenas dados
})

app.head("/", (req, res) => {
    res.send(`Esta é uma requisição HEAD.`) // O método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta, apenas o cabeçalho.
})

app.post("/", (req, res) => {
    res.send(`Esta é uma requisição POST. `) // O método POST é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
})

app.put("/", (req, res) => {
    res.send(`Esta é uma requisição PUT.`) // O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
})

app.patch("/", (req, res) => {
    res.send(`Esta é uma requisição PATCH.`) // Semelhante ao PUT, aplica modificações parciais a um recurso.
})

app.delete("/", (req, res) => {
    res.send(`Esta é uma requisição DELETE.`) // O método DELETE remove o recurso especificado.
})

app.options("/", (req, res) => {
    res.send(`Esta é uma requisição OPTIONS.`) // Retorna as opções de requisição permitidas para um determinado recurso em um servidor.
})

app.listen(8080, () => {
    console.log("SERVIDOR RODANDO")
})

/* A Web Services Description Language (WSDL) é uma linguagem baseada em XML utilizada para descrever 
 Web Services funcionando como um contrato do serviço. 
 Trata-se de um documento escrito em XML que além de descrever o serviço, 
 especifica como acessá-lo e quais as operações ou métodos disponíveis. */