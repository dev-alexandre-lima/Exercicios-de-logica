def checar_item(item):
    if item == 'Espada' or item == 'Escudo' or item == "equipáveis":
        return True
    else:
        return False

def adicionar_ao_enventario(item_encontrado):
    checar_item(item_encontrado)
    if checar_item:
        print(f"{item_encontrado} equipado!")
    else:
        print(f"{item_encontrado} equipado!")

adicionar_ao_enventario("Espada!")
adicionar_ao_enventario("Maçã!")