# 8) Escreva um programa que determine o número de dias e de horas que uma pessoa já viveu.
# Considere que um mês tem 30 dias.

idade=int(input('Informe sua idade: '))

dias= idade * 365
horas= idade * (24 * 365)

print ('Você já viveu:', dias, 'dias e', horas, 'horas!')