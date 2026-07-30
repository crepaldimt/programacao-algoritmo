km = float(input("Quantidade de km percorridos: "))
dias = int(input("Quantidade de dias de aluguel: "))

custo_total = (dias * 60) + (km * 0.15)

print(f"Total a pagar: R$ {custo_total:.2f}")
