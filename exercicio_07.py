temperatura = [25, 30, 27, 22, 30, 19, 23]

# Você percebeu que o termômetro estava errado no primeiro dia (índice 0). Altere o valor de 25 para 26 .
temperatura[0] = 26

#Use a função count() para descobrir e imprimir quantos dias fizeram exatamente 30 graus.
dias_30_graus = temperatura.count(30)
print(dias_30_graus)  # Saída: 2

#. Chegou uma nova leitura de hoje. Use o append()para adicionar 24 graus ao final da lista.
temperatura.append(24)

# Imprima a temperatura máxima e a mínima registrada na lista (Dica: use max() e min()).
temperatura_maxima = max(temperatura)
temperatura_minima = min(temperatura)

print(temperatura_maxima)  # Saída: 30
print(temperatura_minima)  # Saída: 19

# Calcule a média das temperaturas (Some todas as temperaturas e divida pelo tamanho da
# lista) e imprima o resultado.
media_temperatura = sum(temperatura) / len(temperatura)
print(media_temperatura)  # Saída: 24.5

print(temperatura)  # Saída: [26, 30, 27, 22, 30, 19, 23, 24]