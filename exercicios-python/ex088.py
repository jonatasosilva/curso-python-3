from random import randint
from time import sleep
jogos = []
jogo = []
print('-'*30)
print('      JOGA NA MEGA SENA     ')
print('-'*30)
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
for cont in range(0, njogos):
    for c in range(0, 6):
        while True:
            valor = randint(1, 60)
            if valor not in jogo:
                jogo.append(valor)
                break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print('-='*3, f'SORTEANDO {njogos} JOGOS', '-='*3)
for cc in range(0, njogos):
    print(f'Jogo {cc+1}: {jogos[cc]}')
    sleep(1)
print('-='*5, ' < BOA SORTE! > ', '-='*5)
