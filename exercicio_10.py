# Atividade 2: O Cadastro do Console
# Escreva um código que represente um produto específico:
# 1. Crie um dicionário chamado 
# console com as seguintes chaves e valores:
# "nome" : "PlayStation 5"
# "marca" : "Sony"
# "preco" : 4500.00
# 2. Acesse e imprima apenas a marca do console.
# 3. O preço caiu! Altere o valor da chave "preco" para 4200.00.
# 4. Adicione uma nova chave chamada "estoque" com o valor 15.
# 5. Use um loop for para imprimir todas as chaves do dicionário (dica: use .keys()).


console = {
    "nome": "PlayStation 5",
    "marca": "Sony",
    "preco": 4500.00
}

print(console["marca"])

console["preco"] = 4200.00

console["estoque"] = 15

for chave in console.keys():
    print(chave)