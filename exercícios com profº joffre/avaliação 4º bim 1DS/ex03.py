################################################################
# Descrição: Soma e calcula a média de valores não negativos.  #
# Parâmetros de entrada: Reais; número negativo encerra.       #
# Valores de saída: Somatório, média e quantidade de valores.  #
# Autor: Matheus Crepaldi                                      #
################################################################


def ler_real(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    soma = 0.0
    quantidade = 0

    while True:
        valor = ler_real("Digite um valor (negativo para encerrar): ")
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


if __name__ == "__main__":
    main()
