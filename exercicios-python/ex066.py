quant = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'A soma dos {quant} valores foi {soma}!')
