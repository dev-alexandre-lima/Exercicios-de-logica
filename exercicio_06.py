# Desafio final: A Batalha contra o dragão

# Vamos juntos para uma "batalha"!
# Objetivo: Usar múltiplas funções de forma coordenada.

# Tarefa:

from random import randint

def rolar_dado(lados):
    return randint(1, lados)

def calcular_ataque(forca_heroi):
    valor_base = rolar_dado(20)
    dano_total = valor_base + forca_heroi
    return dano_total

def defender(vida_dragao, dano_recebido):
    nova_vida = dano_recebido - vida_dragao
    print(f'O dragão levou {dano_recebido} de dano! Vida restante: {nova_vida}')
    return nova_vida

vida_atual_dragao = 100
minha_forca = 10

for turno in range(3):
    print(f'Turno {turno + 1}: ')
    dano_do_turno = calcular_ataque(minha_forca)
    defender(vida_atual_dragao, dano_do_turno)
    
print("Batalha encerrada!")