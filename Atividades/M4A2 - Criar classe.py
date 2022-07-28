#Instruções do projeto
#Crie uma classe de sua preferência com, no mínimo, uma variável, 
# um método e um incremento. Depois, desenvolva três ou mais 
# objetos para testar o código.

# Inicio do código

class Atletas:

    total_atletas = 0

    def __init__(self):
        self.nome = ''
        self.registro = 0
        self.medalhas = 0

    def cadastro(self, nome, registro, medalhas):
        self.nome = nome
        self.registro = registro
        self.medalhas = medalhas

        Atletas.total_atletas = Atletas.total_atletas + 1

    def imprimir(self):
        print('Nome: {}'.format(self.nome))
        print('Registro: {}'.format(self.registro))
        print('Medalhas: {}'.format(self.medalhas))


atleta1 = Atletas()
atleta1.cadastro('João', 5120, 6)
atleta1.imprimir()

atleta2 = Atletas()
atleta2.cadastro('Maria', 6468, 4)
atleta2.imprimir()

atleta3 = Atletas()
atleta3.cadastro('Curupira', 9746, 27)
atleta3.imprimir()

print('Temos um total de {} atletas cadastrados'.format(Atletas.total_atletas))