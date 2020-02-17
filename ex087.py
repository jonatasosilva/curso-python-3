matriz = [[], [], []]
pares = terceiracoluna = segundalinha = 0
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        if valor % 2 == 0:
            pares += valor
        if j == 2:
            terceiracoluna += valor
        if i == 1 and valor > segundalinha:
            segundalinha = valor
        matriz[i].insert(j, valor)
print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceiracoluna}.')
print(f'O maior valor da segunda linha é {segundalinha}.')
