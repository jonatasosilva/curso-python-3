print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    precofinal = preco - (preco*10/100)
elif opcao == 2:
    precofinal = preco - (preco*5/100)
elif opcao == 3:
    precofinal = preco
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS.'.format(preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    precofinal = preco + (preco*20/100)
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS.'.format(parcelas, precofinal/parcelas))
else:
    precofinal = preco
    print('OPÇÃO INVÁLIDA de pagemento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, precofinal))
