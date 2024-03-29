/*
1. Client-Server
É a restrição básica para uma aplicação REST. 

O objetivo desta divisão é separar a arquiterura e responsabilidades em dois ambientes. 
Assim, o cliente (consumidor do serviço) não se preocupa com tarefas do tipo: 
comunicação com banco de dados, gerenciamento de cache, log, etc. 

E o contrário também é válido, o servidor (provedor do serviço) não se preocupa com tarefas como: 
interface, experiência do usuário, etc. Permitindo, assim, a evolução independente das duas arquiteturas.

2. Stateless
Um mesmo cliente pode mandar várias requisições para o servidor, porém, cada uma delas devem ser
independentes, ou seja, toda requisição deve conter todas as informações necessárias para que o 
servidor consiga entendê-la e processá-la adequatamente.

3. Cacheable
Como muitos clientes acessam um mesmo servidor, e muitas vezes requisitando os mesmos recursos, 
é necessário que estas respostas possam ser cacheadas, evitando processamento desnecessário 
e aumentando significativamente a performance.

4. Uniform Interface
É, basicamente, um contrato para comunicação entre clientes e servidor. 
São pequenas regras para deixar um componente o mais genérico possível, 
o tornando muito mais fácil de ser refatorado e melhorado.

5. Layered System
A sua aplicação deve ser composta por camadas, e estas camadas devem ser fáceis de alterar, 
tanto para adicionar mais camadas, quanto para removê-las. Dito isso, um dos princípios 
desta restrição é que o cliente nunca deve chamar diretamente o servidor da aplicação 
sem antes passar por um intermediador, no caso, pode ser um load balancer ou qualquer 
outra máquina que faça a interface com o(s) servidor(es).

6. Code-On-Demand (Opcional)
Esta condição permite que o cliente possa executar algum código sob demanda, 
ou seja, estender parte da lógica do servidor para o cliente, seja através de um applet ou scripts. 
Assim, diferentes clientes podem se comportar de maneiras específicas mesmo que utilizando 
exatamente os mesmos serviços providos pelo servidor.
*/
