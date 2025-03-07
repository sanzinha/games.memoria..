print ('*********************************************')
print ('Bem vindo ao memoria, seu jogo de adivinhação')
print ('*********************************************')

numero_secreto = 7
total_de_tentativas = 4

for rodada in range (1,total_de_tentativas + 1):
    print(f'tentativas {rodada} de {total_de_tentativas}')
    chute = int(input('digite o seu numero'))

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto



    print (f'Você  digitou {chute} ')

    if(acertou):
        print('Você acertou!')
        break
    else:
        if(chute_maior):
            print('Você errou! Seu número foi maior do que o número secreto')
        elif(chute_menor):
            print('memoria fraca <3, seu número é menor do que o número secreto.')
        
print('@@@@@@@@@@@')
print('Fim de jogo')
print('@@@@@@@@@@@')