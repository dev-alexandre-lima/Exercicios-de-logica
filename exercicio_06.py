# Desafio final: A Batalha contra o dragão


# Vamos juntos para uma "batalha"!
# Objetivo: Usar múltiplas funções de forma coordenada.

# Tarefa:

from random import randint

def rolar_dado(lados = 20):
    return randint(1, lados)

def calcular_ataque(forca_heroi):
    valor_base = rolar_dado(20)
    dano_total = valor_base + forca_heroi
    return dano_total

def defender(vida_dragao, dano_recebido):
    nova_vida = dano_recebido - vida_dragao
    print(f'O dragão levou {dano_recebido} de dano! Vida restante: {nova_vida}')

def vida_atual_dragao(vida_dragao):
    print(f"Vida atual do dragão {vida_dragao}")
    return vida_dragao

def minha_forca(forca):
    print(f"Força do heroi: {forca}")
    return forca

vida_atual_dragao = 100
minha_forca = 70

for turno in range(3):
    dano_do_turno = calcular_ataque(minha_forca)
    defender(vida_atual_dragao, dano_do_turno)
    
    vida_atual_dragao()

    
print("Batalha encerrada!")