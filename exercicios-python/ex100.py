from random import randint
from time import sleep

def sorteia(lst):
    print('Somando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)   
        print(f'{n} ', end='', flush=True)
        sleep(0.3)     
    print('PRONTO!')

def somarPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}.')

numeros = list()

sorteia(numeros)
somarPar(numeros)
