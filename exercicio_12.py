# Parte 4: Desafio Integrado (Listas + Dicionários)
# Cenário: Você tem um sistema de inventário onde cada item da lista é um objeto completo (dicionário).
# Objetivo: Praticar a combinação de listas e dicionários para representar dados mais complexos.
# Questões Práticas
# Questão 1: O Inventário
# Crie uma lista vazia chamada estoque_loja. Em seguida, crie 3 dicionários representando produtos diferentes (cada um deve ter nome e preco). Use o .apend() para colocar esses três dicionários dentro da lista estoque_loja.

# Questão 2: O Caixa
# Percorra a lista estoque_loja usando um for. Para cada produto, imprima uma frase como:"O produto [Nome] custa R$ [Preco]".
# Questão 3: O Valor Total (Lógica)
# Crie uma variável total_patrimonio = 0. Faça um loop na lista e some o preço de todos os produtos nessa variável. No final, mostre o valor total do estoque da loja.

# Resolução:
estoque_loja = []
produto1 = {"nome": "Notebook", "preco": 3500.00}
produto2 = {"nome": "Smartphone", "preco": 2500.00}
produto3 = {"nome": "Tablet", "preco": 1500.00}
estoque_loja.append(produto1)
estoque_loja.append(produto2)
estoque_loja.append(produto3)
for produto in estoque_loja:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")
total_patrimonio = 0
for produto in estoque_loja:
    total_patrimonio += produto["preco"]
print(f"Valor total do estoque da loja: R$ {total_patrimonio:.2f}")
