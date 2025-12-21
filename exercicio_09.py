# Parte 3: Dominando Dicionários (A Ficha do Produto)
# Agora que sabemos listar nomes, precisamos de detalhes. Listas são ordenadas por números
# (índices), mas dicionários são organizados por chaves (nomes dos campos).
# Objetivo: Entender o conceito de Chave: Valor (Key: Value).
# Atividade 1: O Carrinho de Compras (Lista de Dicionários)
# Objetivo: Iterar sobre uma lista onde cada item é um dicionário.
# Enunciado: Você tem uma lista que representa um carrinho de compras de um site.
# carrinho = [
# {"nome": "Camiseta", "preco": 50.00, "quantidade": 2},
# {"nome": "Tênis", "preco": 200.00, "quantidade": 1},
# {"nome": "Meia", "preco": 15.00, "quantidade": 3}
# ]
# Escreva um programa que:
# 1. Percorra a lista carrinho;
carrinho = [
    {"nome": "Camiseta", "preco": 50.00, "quantidade": 2},
    {"nome": "Tênis", "preco": 200.00, "quantidade": 1},
    {"nome": "Meia", "preco": 15.00, "quantidade": 3}
]
# 2. Para cada produto, calcule o subtotal (preço multiplicado pela quantidade).
total_compra = 0
for produto in carrinho:
    subtotal = produto["preco"] * produto["quantidade"]
    total_compra += subtotal
    print(f"Produto: {produto['nome']}, Subtotal: R$ {subtotal:.2f}")
    
# 3. Some todos os subtotais para encontrar o Total da Compra e imprima o valor final.
print(f"Total da Compra: R$ {total_compra:.2f}")