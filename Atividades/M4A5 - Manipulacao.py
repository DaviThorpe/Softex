# Instruções do projeto
# Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado.

# Inicio do código

nome = input('Insira seu nome: ')

maius = nome.upper()
minus = nome.lower()
cont = len(nome)

print('Esse é seu nome maiusculo {}'.format(maius))
print('Esse é seu nome minusculo {}'.format(minus))
print('Seu nome possui {} caracteres'.format(cont))