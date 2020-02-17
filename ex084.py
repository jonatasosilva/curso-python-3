princ = []
temp = []
maior = menor = 0
pesadas = []
leves = []
while True:

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]


    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

for pessoas in princ:
    if pessoas[1] == maior:
        pesadas.append(pessoas[0])
    if pessoas[1] == menor:
        leves.append(pessoas[0])
    

print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de {pesadas}')
print(f'O menor peso foi {menor}Kg. Peso de {leves}')
