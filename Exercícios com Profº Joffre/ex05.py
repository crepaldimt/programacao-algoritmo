################################################################
# Descrição: Calcula o quociente inteiro por subtrações.       #
# Parâmetros de entrada: Dividendo e divisor inteiros.         #
# Valores de saída: Quociente da divisão, truncado para zero.  #
# Autor: Matheus Crepaldi                                      #
################################################################


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def main():
    dividendo = ler_inteiro("Digite o dividendo: ")
    divisor = ler_inteiro("Digite o divisor (diferente de zero): ")
    while divisor == 0:
        print("O divisor não pode ser zero.")
        divisor = ler_inteiro("Digite o divisor (diferente de zero): ")

    # As subtrações são feitas com valores absolutos; o sinal é aplicado ao final.
    resto = abs(dividendo)
    divisor_absoluto = abs(divisor)
    quociente_absoluto = 0

    while resto >= divisor_absoluto:
        resto -= divisor_absoluto
        quociente_absoluto += 1

    if (dividendo < 0) != (divisor < 0):
        quociente = -quociente_absoluto
    else:
        quociente = quociente_absoluto

    print(f"Quociente inteiro: {quociente}")


if __name__ == "__main__":
    main()
