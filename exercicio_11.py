# Atividade 3: O Boletim Escolar (Dicionário Simples)
# Objetivo: Criar, acessar e modificar um dicionário.
# Enunciado:
# 1. Crie um dicionário chamado boletim
#  com as seguintes matérias e notas:
# "Matemática": 8.5
# "Português": 9.0
# "História": 7.5
# 2. O professor de História deu um ponto extra. Atualize a nota de "História" para 8.5
# 3. Adicione uma nova matéria "Geografia" com a nota 10.0
# 4. Calcule a média das notas (somas dos valores dividida pelo número de matérias) e  imprima o resultado

boletim = {
    "Matemática": 8.5,
    "Português": 9.0,
    "História": 7.5
}
boletim["História"] = 8.5
boletim["Geografia"] = 10.0

media_notas = sum(boletim.values()) / len(boletim)
print(media_notas)  # Saída: 9.0

print(boletim)  # Saída: {'Matemática': 8.5, 'Português': 9.0, 'História': 8.5, 'Geografia': 10.0}