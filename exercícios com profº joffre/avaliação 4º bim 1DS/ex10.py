################################################################
# Descrição: Conta os elementos ímpares e o percentual.        #
# Parâmetros de entrada: 10 inteiros para o vetor A.           #
# Valores de saída: Total de ímpares e percentual.             #
# Autor: Matheus Crepaldi                                      #
################################################################

impar = []
vetor_a = []
for indice in range(1, 11):
    valor = int(input(f"A[{indice}]: "))
    vetor_a.append(valor)

for i in vetor_a:
    if i % 2 != 0:
        impar.append(i)

percentual = (len(impar) / 10) * 100

print(f"Total de elementos ímpares: {len(impar)}")
print(f"Percentual de números ímpares: {percentual}%")
print(f"Lista de ímpares: {impar}")
