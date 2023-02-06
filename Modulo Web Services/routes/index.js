const express = require('express')
const jogos = require("./jogosRoutes.js")

const routes = (app) => {
    app.route('/').get((req, res) => {
        res.status(200).send({titulo: "Curso de node"})
    })

    app.use(
        express.json(),
        jogos
    )
}

modeule.exports = routes
