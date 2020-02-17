resp = 'S'
soma = total = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]'))
media = soma/total
print('Você digitou {} números e a media foi {:.2f}'.format(total, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
