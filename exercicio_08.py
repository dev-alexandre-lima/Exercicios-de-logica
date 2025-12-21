# Parte 2: Dominando Listas (O Estoque Simples)
# Nesta etapa, vamos focar apenas em criar uma sequência de itens usando listas. Imagine que
# você está organizando a prateleira da loja.
# Objetivo: Praticar a criação, adição, remoção e ordenação de dados.
# Atividade: A Prateleira de Jogos
# Escreva um código que faça o seguinte:
# 1. Crie uma lista vazia chamada jogos.
jogos = []

# 2. Use o comando appendpara adicionar os seguintes jogos, um por um: "Mario Kart", "Zelda", "Pokemon".
jogos.append("Mario Kart")
jogos.append("Zelda")
jogos.append("Pokemon")

# 3. Use o comando insert para adicionar "Cyberpunk" na primeira posição (índice 0) da lista.
jogos.insert(0, "Cyberpunk")

# 4. A loja vendeu o último jogo da prateleira. Use o comando pop para removê-lo.
jogos.pop()
# 5. Um cliente perguntou se tem "Zelda" na lista. Use o operador False.
tem_zelda = "Zelda" in jogos
print(tem_zelda)  # Saída: True
# 6. Use o comando sort para organizar a lista em ordem alfabética.
jogos.sort()
# 7. Imprima a lista final de jogos.
print(jogos)  # Saída: ['Cyberpunk', 'Mario Kart', 'Zelda']