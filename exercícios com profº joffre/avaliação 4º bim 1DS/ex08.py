################################################################
# Descrição: Transforma valores de acordo com o índice.        #
# Parâmetros de entrada: 15 elementos reais para o vetor A.    #
# Valores de saída: Elementos do vetor B transformados.        #
# Autor: Matheus Crepaldi                                      #
################################################################

vetor_a = []
for indice in range(1, 16):
    valor = float(input(f"Elemento A[{indice}]: ").replace(",", "."))
    vetor_a.append(valor)

vetor_b = []
for indice, valor in enumerate(vetor_a, start=1):
    if indice % 2 == 0:
        vetor_b.append(valor / 2)
    else:
        vetor_b.append(valor * 1.5)

print("Elementos do vetor B:")
print(vetor_b)
