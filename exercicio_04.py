# Exercício 4: O Feitiço "Bola de Fogo" (Parâmetros com Valor Padrão)

# Seu feitiço "Bola de Fogo" é poderoso, mas às vezes você quer uma versão mais fraca para 
# não gastar toda a sua mana.

# Objetivo: Aprender a usar parâmetros com valores padrão (default).
# Tarefa:

# 1. Crie uma função chamada lancar_bola_de_fogo que aceita dois parâmetros: alvo e potencia.
def lancar_bola_de_fogo(alvo, potencia):
    # 3. A deve imprimir: "[alvo] atingido por uma bola de fogo com [potencia] potencia"
    print(f"{alvo} atingido por uma bola de fogo com {potencia} de poder")
    return 
# 2. Defina o valor padrão de potencia para 5.
potencia = 5
# 4. Chame a função de duas maneiras:
# lancar_bola_de_fogo("Esqueleto") (Usará a potencia padraão 5)
lancar_bola_de_fogo("Esqueleto", potencia)
# lanca_bola_de_fogo("Orc chefe", 20) (Usuará a potencia especificada 20)
lancar_bola_de_fogo("Orc Chefe", 20)