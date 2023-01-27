const {criarServer} = require("http");

const PORTA = porecess.env.PORT || 8080;

const servidor = criarServer();

servidor.on("request", (request, response) => {response.en("Olá, Mundo");
});

servidor.listen(PORT, () => {
   console.log('servidor iniciado na porta ${PORTA}'); 
});
