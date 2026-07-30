sal = float(input('Qual o seu salário? '))
aum = float(input('Quantos por cento você quer de aumento? '))

por = sal*(aum/100)
novos = sal+por

print(f'O seu salário novo será de {novos} e terá {por} de aumento.')
