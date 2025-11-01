import numpy as np

from perda_resistencia_temperatura import perda_resist_temp
from calcula_resistencia_compressao import calcula_resist_compres
from calcula_taxa_erosao import calcula_taxa_erosao
from plot_resultados import plot_results

n_sim = 100_000  # Número de simulações

rng = np.random

# Perda de resistência devido às altas temperaturas
p_resist_tempr = perda_resist_temp(n_sim, rng)

# Resistência à compresão
resist_compr = calcula_resist_compres(p_resist_tempr, n_sim, rng)

# Taxa de volume da erosão
taxa_vol_erosao = calcula_taxa_erosao(resist_compr, n_sim, rng)

# Plot
plot_results(p_resist_tempr, resist_compr, taxa_vol_erosao)