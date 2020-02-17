somaidade = 0
maisvelhonome = ''
maisvelhoidade = 0
totmulheres = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if sexo in 'Mn' and idade > maisvelhoidade:
        maisvelhonome = nome
        maisvelhoidade = idade
    if sexo in 'Ff' and idade < 20:
        totmulheres += 1
media = somaidade/4
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelhoidade, maisvelhonome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulheres))
