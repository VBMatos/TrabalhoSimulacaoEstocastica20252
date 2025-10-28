import numpy as np

def perda_resist_erosao(sigma_peso_antes, sigma_peso_depois, sigma_densidade, presist, n_sim):

    # Amostras aleatórias
    fcu_peso_antes = np.random.normal(100, sigma_peso_antes, n_sim) # Média do peso do corpo de prova antes do ciclo
    fcu_peso_depois = np.random.normal(100, sigma_peso_depois, n_sim) # Média do peso do corpo de prova após o ciclo
    fcu_densidade = np.random.normal(100, sigma_densidade, n_sim) # Média da densidade geométrica do refratário

    # Calcula resistência
    return ((fcu_peso_antes - fcu_peso_depois) / fcu_densidade) - presist