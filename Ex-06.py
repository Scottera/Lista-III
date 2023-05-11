# 6) Escreva um programa que calcule o preço final de uma venda, a partir do preço unitário do
# produto, a quantidade vendida e o percentual de desconto.

quant = float(input('Informe a quantidade comprada: '))
precounit = float(input('Informe o valor unitário do produto: '))
desconto = float(input('Informe o percentual de desconto (%): '))

totalSemDesconto = quant * precounit
valortotal = totalSemDesconto - (totalSemDesconto * desconto / 100)

print (f'O valor total do produto é de R$ {valortotal:.2f}')
