################################################################
# Descrição: Exibe as potências de 3 para expoentes de 0 a 15. #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: Potência correspondente a cada expoente.   #
# Autor: Matheus Crepaldi                                      #
################################################################


def main():
    base = 3
    potencia = 1

    # A potência inicial representa 3 elevado a zero.
    for expoente in range(16):
        print(f"3 elevado a {expoente} = {potencia}")
        potencia *= base


if __name__ == "__main__":
    main()
