################################################################
# Descrição: Valida dois vetores e concatena seus elementos.   #
# Parâmetros de entrada: 12 inteiros para cada vetor.          #
# Valores de saída: Vetor C formado pela junção de A e B.      #
# Autor: Matheus Crepaldi                                      #
################################################################


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    vetor_a = []
    print("Vetor A: informe inteiros divisíveis por 2 ou por 3.")
    for indice in range(1, 13):
        while True:
            valor = ler_inteiro(f"A[{indice}]: ")
            if valor % 2 == 0 or valor % 3 == 0:
                vetor_a.append(valor)
                break
            print("Valor inválido: precisa ser divisível por 2 ou por 3.")

    vetor_b = []
    print("Vetor B: informe inteiros que não sejam múltiplos de 5.")
    for indice in range(1, 13):
        while True:
            valor = ler_inteiro(f"B[{indice}]: ")
            if valor % 5 != 0:
                vetor_b.append(valor)
                break
            print("Valor inválido: múltiplos de 5 não são aceitos.")

    vetor_c = vetor_a + vetor_b
    print("Elementos do vetor C:")
    print(vetor_c)


if __name__ == "__main__":
    main()
