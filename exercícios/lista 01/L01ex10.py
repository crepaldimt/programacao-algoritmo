cigarros_dia = int(input("Cigarros fumados por dia: "))
anos_fumando = int(input("Anos fumando: "))

total_cigarros = cigarros_dia * anos_fumando * 365
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440

print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida.")
