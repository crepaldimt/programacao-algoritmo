################################################################
# Descrição: Calcula o quociente inteiro por subtrações.       #
# Parâmetros de entrada: Dividendo e divisor inteiros.         #
# Valores de saída: Quociente da divisão, truncado para zero.  #
# Autor: Matheus Crepaldi                                      #
################################################################

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor (diferente de zero): "))

while divisor == 0:
    print("O divisor não pode ser zero.")
    divisor = int(input("Digite o divisor (diferente de zero): "))

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
