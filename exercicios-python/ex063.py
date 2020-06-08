print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    c += 1
    t1 = t2
    t2 = t3
print('FIM')