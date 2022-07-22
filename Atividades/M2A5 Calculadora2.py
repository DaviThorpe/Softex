# Instruções do projeto
# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
# Depois precisa executar a operação e mostrar o resultado na tela. 
# Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

#Inicio do código

def calculadora (num1, num2, num3):
    if num3 == 1:
        conta = (num1 + num2)
    elif num3 == 2:
        conta = (num1 - num2)
    elif num3 == 3:
        conta = (num1 * num2)
    elif num3 == 4:
        conta = (num1 / num2)
    elif num3 == 0:
        conta = str('Calculadora encerrada')
    else:
        conta = str('Essa opção não exite')
    return conta

num3 = ''
while num3 != 0:
    print('Escolha uma das opções abaixo: \n1: Soma, \n2: Subtração, \n3: Multiplicação, \n4: Divisão, \n0: Sair')
    num3 = float(input('Digite um valor para escolher a operação: '))
    num1 = float(input('Insira um número: '))
    num2 = float(input('Insira outro número: '))
    resultado = calculadora(num1, num2, num3)
    print(resultado)
