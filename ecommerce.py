def calcular_desconto(preco, cupom_desconto):
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")

    desconto = 0

    if cupom_desconto == "OFF50" and preco > 600:
        desconto = 0.50
    elif cupom_desconto == "QUERO20":
        desconto = 0.20
    elif preco >= 100:
        desconto = 0.10

    total = preco * (1 - desconto)

    if total < 150:
        total += 15

    return total