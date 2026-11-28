################################################################
# Descrição: Valida dois vetores e concatena seus elementos.   #
# Parâmetros de entrada: 12 inteiros para cada vetor.          #
# Valores de saída: Vetor C formado pela junção de A e B.      #
# Autor: Matheus Crepaldi                                      #
################################################################

vetor_a = []
print("Vetor A: informe inteiros divisíveis por 2 ou por 3.")
for indice in range(1, 13):
    while True:
        valor = int(input(f"A[{indice}]: "))
        if valor % 2 == 0 or valor % 3 == 0:
            vetor_a.append(valor)
            break
        print("Valor inválido: precisa ser divisível por 2 ou por 3.")

vetor_b = []
print("Vetor B: informe inteiros que não sejam múltiplos de 5.")
for indice in range(1, 13):
    while True:
        valor = int(input(f"B[{indice}]: "))
        if valor % 5 != 0:
            vetor_b.append(valor)
            break
        print("Valor inválido: múltiplos de 5 não são aceitos.")

vetor_c = vetor_a + vetor_b
print("Elementos do vetor C:")
print(vetor_c)
