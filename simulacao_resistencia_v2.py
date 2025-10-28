import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# PARÂMETROS MÉDIOS E INCERTEZAS
# ----------------------------
N = 10_000  # número de simulações

# Valores médios e desvios (defina com base em ensaios reais)
fcu_high_mean, fcu_high_std = 50, 2        # MPa
fcu_room_mean, fcu_room_std = 60, 3        # MPa

P_mean, P_std = 20000, 500                 # N
A_mean, A_std = 0.005, 0.0001              # m²

P1_mean, P1_std = 1000, 10                 # g
P2_mean, P2_std = 950, 10                  # g
dma_geom_mean, dma_geom_std = 1.0, 0.02    # adimensional

# ----------------------------
# 1. Geração estocástica (Máxima Entropia → Normal)
# ----------------------------
rng = np.random.default_rng()

fcu_high = rng.normal(fcu_high_mean, fcu_high_std, N)
fcu_room = rng.normal(fcu_room_mean, fcu_room_std, N)

P = rng.normal(P_mean, P_std, N)
A = rng.normal(A_mean, A_std, N)

P1 = rng.normal(P1_mean, P1_std, N)
P2 = rng.normal(P2_mean, P2_std, N)
dma_geom = rng.normal(dma_geom_mean, dma_geom_std, N)

# ----------------------------
# 2. Cálculos principais
# ----------------------------
Presist = (fcu_high - fcu_room) / fcu_room
Rcomp = (P / A) - Presist
VE = ((P1 - P2) / dma_geom) - (Presist * Rcomp)


# ----------------------------
# 3. Estatísticas de saída
# ----------------------------
print(f"Presist médio = {np.mean(Presist):.4f}")
print(f"Rcomp médio = {np.mean(Rcomp):.2f} MPa")
print(f"VE médio = {np.mean(VE):.4f} cm³")
print(f"Desvio de VE = {np.std(VE):.4f} cm³")


# ----------------------------
# 4. Visualização (Distribuições)
# ----------------------------
plt.figure(figsize=(6, 8))
plt.subplot(3, 1, 1)
plt.hist(Presist, bins=50, color='skyblue', alpha=0.7)
plt.title('Distribuição da Perda de Resistência Após Altas Temperaturas')

plt.subplot(3, 1, 2)
plt.hist(Rcomp, bins=50, color='salmon', alpha=0.7)
plt.title('Distribuição da Resistência à Compressão em Altas Temperaturas')

plt.subplot(3, 1, 3)
plt.hist(VE, bins=50, color='lightgreen', alpha=0.7)
plt.title('Distribuição da Taxa de Erosão')

plt.tight_layout()
plt.show()