import random

num = [random.randint(1, 100) for _ in range(20)]
par = []
imp = []

for numero in num:
    if numero % 2 != 0:
        imp.append(numero)

    else:
        par.append(numero)


print(f'Números selecionados: {num}\n'
      f'Par: {par}\n'
      f'Ímpar: {imp}')
