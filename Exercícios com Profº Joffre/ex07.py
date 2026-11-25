################################################################
# Descrição: Cria somatórios de 1 até cada valor de A.         #
# Parâmetros de entrada: 20 elementos inteiros para o vetor A. #
# Valores de saída: Vetor B com os somatórios calculados.      #
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
    for indice in range(1, 21):
        vetor_a.append(ler_inteiro(f"Elemento A[{indice}]: "))

    vetor_b = []
    for valor in vetor_a:
        soma = 0
        for numero in range(1, valor + 1):
            soma += numero
        vetor_b.append(soma)

    print("Elementos do vetor B:")
    print(vetor_b)


if __name__ == "__main__":
    main()
