peso = float(input('Quantos quilos você pescou? '))
reg = peso-50

if peso > 50:
    print(f'Você terá que pagar R${reg*4.00} por conta de exceder o peso máximo do estado em {reg}kg.')

else:
    print(f'Você pescou {peso}kg e não pagará impostos sobre!')
