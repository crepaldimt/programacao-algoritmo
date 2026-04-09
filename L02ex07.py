import math

area = float(input('Qual é a área (em m²) que vai ser pintada?  '))
tint = area / 3

latas = math.ceil(tint/18)
precot = latas*80.00

if latas <= 0 or area <= 0 or tint <= 0:
    print('Valores inseridos errado.')

else:
    print(f'Você comprará {latas} latas e pagará R${precot}')
