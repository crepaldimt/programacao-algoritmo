anoa = int(input('Qual ano estámos? '))

if anoa%400 == 0:
          print(f'O ano de {anoa} é bissexto')

elif anoa%100 == 0:
        print(f'O ano de {anoa} não é bissexto!')
elif anoa%4 == 0:
    print(f'O ano de {anoa} é bissexto!')

else:
    print(f'O ano de {anoa} não é bissexto.')
