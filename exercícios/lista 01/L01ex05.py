preco = float(input("Preço da mercadoria: R$ "))
percentual = float(input("Percentual de desconto (%): "))

valor_desconto = preco * (percentual / 100)
preco_a_pagar = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
