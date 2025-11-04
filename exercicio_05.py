# Exercício: 5 o Inventário do Aventureiro(Combinando Funções)

# Um bom aventureiro organiza sua mochila. Vamos usar funções para gernciar o que encontramos.

# Objetivo: Ver como funções podem chamar outras funções
# Tarefa:

# 1. Primeiro, crie um função checar_item(item) que retorna True se o item for "Espada" ou "Escudo" e False para que outra coisa (esses são seus itens "equipaveis")
def checar_item(item):
    if item == 'Espada' or item == 'Escudo':
        return True
    else:
        return False
# 2. Em seguida, crie uma função principal chama adicionar_ao_inventario(item_encontrado).
def adicionar_ao_enventario(item_encontrado):
    # 3. Dentro de adicinar_ao_inventario:
    # Ele deve chamar a função checar_item(item_encontado)
    checar_item(item_encontrado)
    # Se checar_item retornar True, imprima "[item_encontado] equidado!"
    if checar_item:
        print(f"{item_encontrado} guardado na mochila!")
    # Se retonar False, imprima '[item_encontrado] guardado na mochila.'
    else:
        print(f"{item_encontrado} equipado!")
# 4. Teste chamando adicionar_ao_inventario("Espada")
adicionar_ao_enventario("Espada!")
# adicionar_ao_inventario("Espada")
adicionar_ao_enventario("Maçã!")
adicionar_ao_enventario("Diamente!")