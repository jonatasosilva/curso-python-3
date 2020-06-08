salario = float(input('Qual é o salário do funcionário? R$ '))
novosalario = 0
if salario > 1250:
    novosalario = salario*1.10
else:
    novosalario = salario*1.15
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novosalario))