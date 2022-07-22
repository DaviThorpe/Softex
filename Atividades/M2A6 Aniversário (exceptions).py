# Instruções do projeto
# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. 
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Inicio do código


nasc_certo = False

while (nasc_certo == False):
    try:
        nome = str(input('Insira seu nome: '))
        nasc = int(input('Insira seu ano de nascimento: '))
        if nasc >= 1922 and nasc <= 2021:
            nasc_certo = True
            idade = 2022 - nasc
            print('{0} terá {1} em 2022'.format(nome, idade))
        else:
            print('Erro!! Você deve digitar um ano entre 1922 e 2021')
    except:
        print('Você digitou algo inválido')
