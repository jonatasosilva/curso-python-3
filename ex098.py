from time import sleep

def contador(i, f, p=1):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        for c in range (i, f+1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for c in range (i, f-1, (-p)):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print('FIM!')

contador(1, 10)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
contador(inicio, fim, passo)
