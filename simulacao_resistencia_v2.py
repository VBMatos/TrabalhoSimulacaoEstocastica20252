import numpy as np
import matplotlib.pyplot as plt

from perda_resistencia_temperatura import perda_resist_temp
from calcula_resistencia_compressao import calcula_resist_compres
from calcula_taxa_erosao import calcula_taxa_erosao


n_sim = 100_000  # Número de simulações

rng = np.random.default_rng()

# Perda de resistência devido às altas temperaturas
p_resist_tempr = perda_resist_temp(n_sim, rng)

# Resistência à compresão em altas temperaturas
resist_compr = calcula_resist_compres(p_resist_tempr, n_sim, rng)

# Taxa de volume da erosão
taxa_vol_erosao = calcula_taxa_erosao(resist_compr, n_sim, rng)

print(f"Média da Perda de Resitência = {np.mean(p_resist_tempr):.3f}")
print(f"Média da Resitência à Compressão = {np.mean(resist_compr):.3f}")
print(f"Média da Taxa de Erosão = {np.mean(taxa_vol_erosao):.3f}")
print(f"Desvio da Taxa de Erosão = {np.std(taxa_vol_erosao):.3f}")


# Plot
plt.figure(figsize=(7, 8))
plt.subplot(3, 1, 1)
plt.hist(p_resist_tempr, bins=50, color='skyblue')
plt.title('Distribuição da Perda de Resistência Após Altas Temperaturas')

plt.subplot(3, 1, 2)
plt.hist(resist_compr, bins=50, color='salmon')
plt.title('Distribuição da Resistência à Compressão em Altas Temperaturas')

plt.subplot(3, 1, 3)
plt.hist(taxa_vol_erosao, bins=50, color='lightgreen')
plt.title('Distribuição da Taxa de Erosão')

plt.tight_layout()
plt.show()