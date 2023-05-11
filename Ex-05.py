# 5) Um mestre de obras deseja trocar o piso de uma casa e gostaria de calcular quanto de
# argamassa e rejunte serão necessários para realizar a obra. Desenvolva um programa que
# receba do usuário a área total da casa (em m2) e calcule como saída:
# • Quantos Kg de rejunte serão utilizados para aplicação (considerar 1Kg para 3m2)
# • Quantos Kg de argamassa serão utilizados para a aplicação (considerar 1kg por 5m2)

area = float(input('Informe o total de m²: '))

rejunte = area / 3
argamassa = area / 5

print(f'Será utilizado {rejunte:.2f} kg de rejunte e')
print(f'Será utilizado também {argamassa:.2f} kg de argamassa!')
