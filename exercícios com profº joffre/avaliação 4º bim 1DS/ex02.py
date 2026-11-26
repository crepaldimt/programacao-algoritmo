################################################################
# Descrição: Calcula os grãos de trigo em um tabuleiro 8 x 8.  #
# Parâmetros de entrada: Nenhum.                               #
# Valores de saída: Grãos finais e total de grãos.             #
# Autor: Matheus Crepaldi                                      #
################################################################

graos_no_quadro = 1
total_graos = 0
graos_no_ultimo_quadro = 0

for quadro in range(1, 65):
    total_graos += graos_no_quadro
    graos_no_ultimo_quadro = graos_no_quadro
    graos_no_quadro *= 2

ultimo_formatado = f"{graos_no_ultimo_quadro:,}".replace(",", ".")
total_formatado = f"{total_graos:,}".replace(",", ".")
print(f"Grãos no 64º quadro: {ultimo_formatado}")
print(f"Total de grãos no tabuleiro: {total_formatado}")
