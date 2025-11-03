# Exercício 4: O Feitiço "Bola de Fogo" (Parâmetros com Valor Padrão)

# Seu feitiço "Bola de Fogo" é poderoso, mas às vezes você quer uma versão mais fraca para 
# não gastar toda a sua mana.

# Objetivo: Aprender a usar parâmetros com valores padrão (default).
# Tarefa:

# 1. Crie uma função chamada lancar_bola_de_fogo que aceita dois parâmetros: alvo e potencia.
def lancar_bola_de_fogo(alvo, potencia):
    potencia = 5
    print(f"{alvo} atingido por uma bola de fogo com {potencia} de poder")
    return 

lancar_bola_de_fogo("Esqueleto")
lancar_bola_de_fogo("Orc Chefe", 20)