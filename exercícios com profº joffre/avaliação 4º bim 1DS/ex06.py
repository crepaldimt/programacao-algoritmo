################################################################
# Descrição: Analisa 20 temperaturas em graus Celsius.         #
# Parâmetros de entrada: 20 valores reais de temperatura.      #
# Valores de saída: Menor, maior e média das temperaturas.     #
# Autor: Matheus Crepaldi                                      #
################################################################

temperaturas = []

for indice in range(1, 21):
    temperatura = float(input(f"Temperatura {indice}/20 em °C: ").replace(",", "."))
    temperaturas.append(temperatura)

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"Menor temperatura: {menor:g} °C")
print(f"Maior temperatura: {maior:g} °C")
print(f"Média das temperaturas: {media:.2f} °C")
