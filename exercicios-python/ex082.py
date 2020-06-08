completa = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    completa.append(n)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for v in completa:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
