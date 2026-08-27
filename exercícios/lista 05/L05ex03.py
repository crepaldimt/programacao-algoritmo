p = []

def par(x):
    if x % 2 == 0:
        if x % 7 == 0:
            p.append(x)

for i in range(1067, 3627):
    par(i)

p = len(p)

print(p)
