# Exercício 3: A Poção de Cura (Retorno de Valor)

# Você não pode apenas falar sobre cura, você precisa que o feitiço lhe devolva pontos de vida!
# Objetivo: Fazer uma função "devolver" um valor usando a palavra-chave return. 
# Tarefa:

#1. Crie uma função chamada preparar_pocao_curaque aceita um parâmetro intensidade(um número).
def preparar_pocao_cura(intensidade):
# 2. A função deve calcular os pontos de vida curados. A fórmula é: 
# pontos_curados = intensidade * 10.
    pontos_curados = intensidade * 10
    # 3. Em vez de imprimir, a funçãõ deve retornar o valor de pontos_curad0.
    return f"A poção foi preparada! Ela cura {pontos_curados} pontos de vida."
# 4. Fora da função:
    #Chame preparar_pocao_cura(5) e amarzene o resulto em uma variavel chamada cura_pequena.
cura_pequena = 5
    #Chame preparar_pocao_cura(10) e amarzene o resulto em uma variavel chamada cura_grande.
cura_grande = 10
    # Imprima os valores de cura_pequena e cura_grande.
print(preparar_pocao_cura(cura_pequena))
print(preparar_pocao_cura(cura_grande))