# Parâmetros de entrada: Reais; número negativo encerra.       #
# Valores de saída: Somatório, média e quantidade de valores.  #
# Autor: Matheus Crepaldi                                      #
################################################################

soma = 0.0
quantidade = 0

while True:
    valor = float(input("Digite um valor (negativo para encerrar): ").replace(",", "."))
    if valor < 0:
        break
    soma += valor
    quantidade += 1

print(f"Somatório: {soma:g}")
print(f"Total de valores lidos: {quantidade}")
if quantidade > 0:
    print(f"Média: {soma / quantidade:g}")
else:
    print("Média: não calculável (nenhum valor não negativo foi informado).")

