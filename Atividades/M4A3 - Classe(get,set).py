# Instruções do projeto
# Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um 
# método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

# A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.

# Inicio do código

class Atleta:

    def __init__(self):
        self.__nome = ''
        self.__medalhas = int()

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        print('Nome do atleta: {} '.format(self.__nome))
        return self.__nome

    def set_medalhas(self, medalhas):
        if medalhas < 0:
            print('Valores menores que zero não são válidos!')
        else:
            self.__medalhas = medalhas

    def get_medalhas(self):
        print('O atleta possui {} medalhas'.format(self.__medalhas))
        return self.__medalhas
    
    def ficha(self):
        print('O atleta {} possui um total de {} medalhas'.format(self.__nome, self.__medalhas))


atleta1 = Atleta()
atleta1.set_nome('Saci')
atleta1.get_nome()

# Testando a condição
atleta1.set_medalhas(-1)
atleta1.get_medalhas()

atleta1.set_medalhas(7)
atleta1.get_medalhas()

# Imprimindo a ficha do atleta
atleta1.ficha()
