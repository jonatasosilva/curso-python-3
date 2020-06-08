from random import randint
pontos = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    tipo = ' '
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. ', end='')
    if total % 2 == 0:
        print(f'TOTAL de {total} DEU PAR')
        resultado = 'P'
    else:
        print(f'TOTAL de {total} DEU ÍMPAR')
        resultado = 'I'
    if tipo == resultado:
        pontos += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
    else:
        print('Você PERDEU!')
        print('=-'*15)
        break
print(f'GAMER OVER! Você venceu {pontos} vezes.')
