'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(b=2, a=5)
soma(3, 7)
'''

'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(1, 4, 5, 7)
contador(8, 0)
contador(4, 4, 7)
'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2, 4, 7, 1]
dobra(valores)
print(valores)
'''

def soma(*valores):
    s = 0
    for v in valores:
        s += v
    print(f'Somando o valores {valores} temos {s}')

soma(5, 8, 2)
soma(3, 6, 4)
