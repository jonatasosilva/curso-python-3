distancia = float(input('Qual é a distância da sua viagem? '))
preco = 0
print('Você está prestes a começar umaviagem de {}Km.'.format(distancia))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
'''if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45'''
print('E o preço de sua passagem será de R$ {:.2f}'.format(preco))