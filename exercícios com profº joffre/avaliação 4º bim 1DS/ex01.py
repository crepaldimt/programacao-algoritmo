################################################################
# Descrição: Exibe as potências de 3 para expoentes de 0 a 15. #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: Potência correspondente a cada expoente.   #
# Autor: Matheus Crepaldi                                      #
################################################################

base = 3
potencia = 1

for expoente in range(16):
    print(f"3 elevado a {expoente} = {potencia}")
    potencia *= base
