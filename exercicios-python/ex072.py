numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
'quinze', 'qezesseis', 'dezessete', 'dezeoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while not (0 <= numero <= 20):
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[numero]}')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA!')