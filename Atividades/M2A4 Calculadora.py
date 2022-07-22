#Instruções do projeto
#Faça uma função calculadora de dois números com três parâmetros: 
#os dois primeiros serão os números da operação e o terceiro 
#será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

#Inicio do código

def calculadora (num1, num2, num3):
    if num3 == 1:
        conta = num1 + num2
    elif num3 == 2:
        conta = (num1 - num2)
    elif num3 == 3:
        conta = (num1 * num2)
    elif num3 == 4:
        conta = (num1 / num2)
    else:
        conta = 0
    return conta

num1 = float(input('Insira um número:'))
num2 = float(input('Insira outro número: '))
num3 = float(input('Insira 1 (soma), 2 (subtração), 3 (multiplicação) ou 4 (divisão): '))
resultado = calculadora(num1, num2, num3)
print('Esse é seu resultado:', resultado)



