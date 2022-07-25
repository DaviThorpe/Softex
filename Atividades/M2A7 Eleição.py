# Instruções do projeto
# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. 
# Caso o número do voto não corresponda a nenhum candidato ou seja branco, 
# ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, 
# o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, 
# aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 

# Inicio do código

votos_candidato_x = int(0)
votos_candidato_y = int(0)
votos_candidato_z = int(0)
votos_brancos = int(0)
votos_nulos = int(0)
votar = True

while votar == True:
    try:
        print('Escolha seu candidato \ncandidato_X: 889 \ncandidato_Y: 847 \ncandidato_Z: 515 \nbranco: 0')
        voto = int(input("Digite o número do seu candidato: "))
        if voto == 889:
                votos_candidato_x = (votos_candidato_x + 1)
        elif voto == 847:
                votos_candidato_y = (votos_candidato_y + 1)
        elif voto == 515:
                votos_candidato_z = (votos_candidato_z + 1)
        elif voto == 0:
                votos_brancos = (votos_brancos + 1)
        else:
                votos_nulos = (votos_nulos + 1)
        fim = int(input('Deseja finalizar a votação ? \nDigite 1 para Sim ou 2 para Não: '))
        if fim == 1:
            votar = False
            print('Votação encerrada')
            if votos_candidato_x > votos_candidato_y and votos_candidato_x > votos_candidato_z:
                print('O vencedor foi o cadidado X com {} votos!'.format(votos_candidato_x))
                print('Votos Candidato Y: {}'.format(votos_candidato_y))
                print('Votos Candidato Z: {}'.format(votos_candidato_z))
                print('Votos Nulos: {}'.format(votos_nulos))
                print('Votos Brancos: {}'.format(votos_brancos))
            elif votos_candidato_y > votos_candidato_x and votos_candidato_y > votos_candidato_z:
                print('O vencedor foi o cadidado y com {} votos!'.format(votos_candidato_y))
                print('Votos Candidato X: {}'.format(votos_candidato_x))
                print('Votos Candidato Z: {}'.format(votos_candidato_z))
                print('Votos Nulos: {}'.format(votos_nulos))
                print('Votos Brancos: {}'.format(votos_brancos))
            elif votos_candidato_z > votos_candidato_x and votos_candidato_z > votos_candidato_y:
                print('O vencedor foi o cadidado z com {} votos!'.format(votos_candidato_z))
                print('Votos Candidato X: {}'.format(votos_candidato_x))
                print('Votos Candidato Y: {}'.format(votos_candidato_y))
                print('Votos Nulos: {}'.format(votos_nulos))
                print('Votos Brancos: {}'.format(votos_brancos))
            elif fim == 2:
                votar = True
    except:
        print('Você deve digitar apenas números')
