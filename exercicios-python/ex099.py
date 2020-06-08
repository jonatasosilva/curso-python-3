from time import sleep

def maior (*valores):
    total = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for pos, v in enumerate(valores):
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if pos == 0:
            maior = v
        else: 
            if v > maior:
                maior = v
        total += 1
    print(f'Foram informados {total} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()