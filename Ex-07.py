# 7) Uma loja deseja calcular o preço final a ser cobrado por uma duplicata. Esta loja aplica uma
# multa de 5% do valor da duplicata para cada dia de atraso.

valdupli = float(input('Informe o valor da duplicata: '))
dias = int(input('Informe os dias de atraso:'))

multa= dias * 0.05
vltotal= valdupli + (valdupli * multa)

print (f'O valor a ser pago pela duplicata é R$ {vltotal:.2f} ')