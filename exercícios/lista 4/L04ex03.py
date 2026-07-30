import random

v1 = [random.randint(1, 100) for _ in range(10)]
v2 = [random.randint(1, 100) for _ in range(10)]

v3 = []
for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])

print(f'Vetor 1 = {v1}\n'
      f'Vetor 2 = {v2}\n'
      f'Vetor 3 = {v3}\n')
