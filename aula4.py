valor_compra = float(input('Valor da compra: '))
pagamento = int(input('Compra no crédito?:\n 1- SIM ou 2- NÃO: '))

if valor_compra > 100 and pagamento == 1:
    valor_compra = valor_compra * 0.9
    print('O cliente tem direito a desconto. O valor final é: {}'.format(valor_compra))
else:
    print('Valor cheio. O valor final é: {}'.format(valor_compra))