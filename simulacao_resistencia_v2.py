import numpy as np
import matplotlib.pyplot as plt

from perda_resistencia_temperatura import perda_resist_temp
from calcula_resistencia_compressao import calcula_resist_compres
from calcula_taxa_erosao import calcula_taxa_erosao
from calcula_entropia import calcula_entropia

n_sim = 100_000  # Número de simulações

rng = np.random.default_rng()

Presist_temp = perda_resist_temp(n_sim, rng)                           # Perda de resistência devido à altas temperaturas
Rcomp = calcula_resist_compres(Presist_temp, n_sim, rng)               # Resistência à compresão
taxa_vol_erosao = calcula_taxa_erosao(Presist_temp, Rcomp, n_sim, rng) # Taxa de volume da erosão

print(f"Presist médio = {np.mean(Presist_temp):.4f}")
print(f"Rcomp médio = {np.mean(Rcomp):.2f} MPa")
print(f"VE médio = {np.mean(taxa_vol_erosao):.4f} cm³")
print(f"Desvio de VE = {np.std(taxa_vol_erosao):.4f} cm³")


# Plot
plt.figure(figsize=(7, 8))
plt.subplot(3, 1, 1)
plt.hist(Presist_temp, bins=50, color='skyblue')
plt.title('Distribuição da Perda de Resistência Após Altas Temperaturas')

plt.subplot(3, 1, 2)
plt.hist(Rcomp, bins=50, color='salmon')
plt.title('Distribuição da Resistência à Compressão em Altas Temperaturas')

plt.subplot(3, 1, 3)
plt.hist(taxa_vol_erosao, bins=50, color='lightgreen')
plt.title('Distribuição da Taxa de Erosão')

plt.tight_layout()
plt.show()