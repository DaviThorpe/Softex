#Instruções do projeto
#Crie uma classe de sua preferência com, no mínimo, uma variável, 
# um método e um incremento. Depois, desenvolva três ou mais 
# objetos para testar o código.

# Inicio do código

total_carros = int()

class estacionamento():
    def __init__(self, bloco, modelo, vaga):
        self.bloco = bloco
        self.modelo = modelo
        self.vaga = vaga
    
    # Método
    def estacionado(self):
        print('O carro número {} está estacionado na vaga {}'.format(estacionamento.total_carros, self.vaga))
    
    # Incremento
    def total ():
        estacionamento.total_carros = (total_carros + 1)
    
    # imprimindo 
    def situacao (self):
        print('O carro modelo: {} está no bloco {}, na vaga {}'.format(self.modelo, self.bloco, self.vaga))

    # Mostrando o total de carros
    def total_car():
        print('O total de carros é: {}'.format(total_carros))

# Testando os objetos

carro_1 = estacionamento('A','honda_civc',1)
carro_1.total()
carro_1.situacao()
carro_1.total_car()