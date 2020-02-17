from random import randint
print('''Sou seu computador...
Acabei de pensar em número entre 0 e 10.
Será que consegue adivinhar qual foi?''')
computador = randint(1, 10)
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
