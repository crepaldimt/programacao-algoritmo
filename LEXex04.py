num1 = float(input('Insire um número: '))
num2 = float(input('Insire um número: '))
op = input('Insire a operação: ')

if op == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif op == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif op == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif op == '/':
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print("Erro: Divisão por zero!")

