nm = input('Insira o nome do aluno: ')
nf = float(input('Insira a nota do aluno: '))

if nf >= 7:
    print('Aprovado')

elif nf >= 5 and nf <= 6.9:
    print('Em recuperação')

else:
    print('Reprovado')
