print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
tot50 = tot20 = tot10 = tot1 = 0
valor = int(input('Que valor você quer sacar? R$'))
while valor != 0:
    while True:
        if valor >= 50:
            valor -= 50
            tot50 += 1
            break
        elif valor >= 20:
            valor -= 20
            tot20 += 1
            break
        elif valor >= 10:
            valor -= 10
            tot10 += 1
            break    
        elif valor >= 1:
            valor -= 1
            tot1 += 1
            break          
if tot50 > 0:
    print(f'Total de {tot50} cédulas de R$50')
if tot20 > 0:
    print(f'Total de {tot20} cédulas de R$20')
if tot10 > 0:
    print(f'Total de {tot10} cédulas de R$10')
if tot1 > 0:
    print(f'Total de {tot1} cédulas de R$1')
