sim = []
nao = []

def numsortudo(x):
    x = str(x)
    if "2" in x and "7" not in x:
        sim.append(x)

for i in range(18643, 33088):
    numsortudo(i)

sim = len(sim)

print(sim)
