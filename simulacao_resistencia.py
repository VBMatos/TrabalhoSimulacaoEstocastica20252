import matplotlib.pyplot as plt
import numpy as np

from perda_resistencia_temperatura import perda_resist_temp
from perda_resistencia_compressao import perda_resist_compres
from perda_resistencia_erosao import perda_resist_erosao

from calcula_entropia import calcular_entropia

# np.random.seed(42)

# Parâmetros
sigma_room = 0
sigma_high = 100
n_sim = 100_000

presist_temp = perda_resist_temp(sigma_room, sigma_high, n_sim)

sigma_carga = 100
sigma_area = 100

presist_compres = perda_resist_compres(sigma_carga, sigma_area, presist_temp, n_sim)

sigma_peso_antes = 100
sigma_peso_depois = 100
sigma_densidade = 100

taxa_erosao = perda_resist_erosao(sigma_peso_antes, sigma_peso_depois, sigma_densidade, presist_temp, n_sim)

k = 10 # Constante de proporcionalidade
entropia = calcular_entropia(presist_temp, presist_compres, k)

print("Presist (array):", np.round(presist_temp, 4))
print("Rcomp (array):", np.round(presist_compres, 4))
print("Entropia (array):", np.round(entropia, 6))

# Plot
plt.figure(1)
plt.hist(presist_temp * 100, bins=50, color='steelblue', alpha=0.7)
plt.xlabel('Perda de resistência (%)')
plt.ylabel('Frequência')
plt.title('Perda de Resistência em Altas Temperaturas')

plt.figure(2)
plt.hist(presist_compres * 100, bins=50, color='steelblue', alpha=0.7)
plt.xlabel('Perda de resistência (%)')
plt.ylabel('Frequência')
plt.title('Perda de Resistência por Compressão (em Altas Temperaturas)')

plt.figure(3)
plt.hist(taxa_erosao * 100, bins=50, color='steelblue', alpha=0.7)
plt.xlabel('Perda de resistência (%)')
plt.ylabel('Frequência')
plt.title('Taxa de Erosão (em Altas Temperaturas)')

plt.show()