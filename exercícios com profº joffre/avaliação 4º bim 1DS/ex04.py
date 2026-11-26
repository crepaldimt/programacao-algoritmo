################################################################
# Descrição: Calcula a área total de uma residência.           #
# Parâmetros de entrada: Nome e dimensões dos cômodos.         #
# Valores de saída: Área de cada cômodo e área total.          #
# Autor: Matheus Crepaldi                                      #
################################################################

area_total = 0.0

while True:
    nome_comodo = input("Nome do cômodo: ")
    largura = float(input("Largura em metros: ").replace(",", "."))
    comprimento = float(input("Comprimento em metros: ").replace(",", "."))
    area_comodo = largura * comprimento
    area_total += area_comodo

    print(f"Área do cômodo {nome_comodo}: {area_comodo:.2f} m²")

    resposta = input("Deseja calcular outro cômodo? (S/N): ").strip().upper()
    if resposta in ("N", "NÃO", "NAO"):
        break

print(f"Área total da residência: {area_total:.2f} m²")
