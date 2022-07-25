# Instruções do projeto
# Crie um tipo abstrato de dado (TAD) para manipular números complexos na
# linguagem Python.
# O método deve:

# - calcular três números complexos;
# - realizar todas as operações básicas;
# - e imprimir as propriedades real e img do números.

# Inicio do código

print('Iremos armazenar os números complexos')
num_1r = int(input('Insira a parte real do primeiro número :'))
num_1i = int(input('Insira a parte imaginária do primeiro número :'))
num_2r = int(input('Insira a parte real do segundo número :'))
num_2i = int(input('Insira a parte imaginária do segundo número :'))
num_3r = int(input('Insira a parte real do terceiro número :'))
num_3i = int(input('Insira a parte imaginária do terceiro número :'))

def op_cplx (num_1r, num_1i, num_2r, num_2i, num_3r, num_3i):
    # Soma dos números complexos
    soma_real = num_1r + num_2r + num_3r
    soma_img = num_1i + num_2i + num_3i
    soma_cplx = '{} {}i'.format(soma_real, soma_img)
    # Subtração dos números complexos
    sub_real = num_1r - num_2r - num_3r
    sub_img = num_1i - num_2i - num_3i
    sub_cplx = '{} {}i'.format(sub_real, sub_img)
    # Multiplicação dos números complexos
    mul_real = num_1r * num_2r * num_3r
    mul_img = num_1i * num_2i * num_3i
    mul_cplx = '{} {}i'.format(mul_real, mul_img)
    # Divisão dos números complexos
    div_real = num_1r / num_2r / num_3r
    div_img = num_1i / num_2i / num_3i
    div_cplx = '{}  {}i'.format(div_real, div_img)

    print('O resultado da soma é: {}. Sendo {} a parte real e {}i a parte imaginaria'.format(soma_cplx, soma_real, soma_img))
    print('O resultado da subtração é: {}. Sendo {} a parte real e {}i a parte imaginaria'.format(sub_cplx, sub_real, sub_img))
    print('O resultado da multiplicação é: {}. Sendo {} a parte real e {}i a parte imaginaria'.format(mul_cplx, mul_real, mul_img))
    print('O resultado da divisão é: {}. Sendo {} a parte real e {}i a parte imaginaria'.format(div_cplx, div_real, div_img))


op_cplx(num_1r, num_1i, num_2r, num_2i, num_3r, num_3i)