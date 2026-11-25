################################################################
# Descrição: Conta os números ímpares em um vetor.             #
# Parâmetros de entrada: 10 elementos inteiros para o vetor A. #
# Valores de saída: Quantidade e percentual de números ímpares.#
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
    for indice in range(1, 11):
        vetor_a.append(ler_inteiro(f"Elemento A[{indice}]: "))

    quantidade_impares = 0
    for valor in vetor_a:
        if valor % 2 != 0:
            quantidade_impares += 1

    percentual_impares = quantidade_impares / len(vetor_a) * 100
    print(f"Total de elementos ímpares: {quantidade_impares}")
    print(f"Percentual de ímpares: {percentual_impares:.2f}%")


if __name__ == "__main__":
    main()
