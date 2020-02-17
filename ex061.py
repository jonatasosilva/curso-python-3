print('Gerador da PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(termo, end=' -> ')
    c += 1
    termo += razao
print('FIM')
