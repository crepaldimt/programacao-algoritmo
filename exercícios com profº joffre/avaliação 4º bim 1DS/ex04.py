################################################################
# Descrição: Calcula a área total de uma residência.           #
# Parâmetros de entrada: Nome e dimensões dos cômodos.         #
# Valores de saída: Área de cada cômodo e área total.          #
# Autor: Matheus Crepaldi                                      #
################################################################


def ler_medida_positiva(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            medida = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite uma medida numérica.")
            continue

        if medida > 0:
            return medida
        print("A medida deve ser maior que zero.")


def deseja_continuar():
    while True:
        resposta = input("Deseja calcular outro cômodo? (S/N): ").strip().casefold()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "não", "nao"):
            return False
        print("Resposta inválida. Digite S para sim ou N para não.")


def main():
    area_total = 0.0

    while True:
        nome_comodo = input("Nome do cômodo: ").strip()
        while not nome_comodo:
            print("O nome do cômodo não pode ficar vazio.")
            nome_comodo = input("Nome do cômodo: ").strip()

        largura = ler_medida_positiva("Largura em metros: ")
        comprimento = ler_medida_positiva("Comprimento em metros: ")
        area_comodo = largura * comprimento
        area_total += area_comodo

        print(f"Área do cômodo {nome_comodo}: {area_comodo:.2f} m²")
        if not deseja_continuar():
            break

    print(f"Área total da residência: {area_total:.2f} m²")


if __name__ == "__main__":
    main()
