import random

num = [random.randint(1, 100) for _ in range(10)]
num.sort()
maior = num[-1:]
menor = num[:1]

print(f'Os números escolhidos foram {num}, sendo {maior} o maior e {menor} o menor.')