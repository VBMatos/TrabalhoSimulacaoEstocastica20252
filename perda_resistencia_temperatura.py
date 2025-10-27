import numpy as np

def perda_resist_temp(sigma_room, sigma_high, n_sim):

    # Gera amostras aleatórias
    fcu_high = np.random.normal(100, sigma_high, n_sim) # Média da resistência após altas temperaturas
    fcu_room = np.random.normal(100, sigma_room, n_sim) # Média da resistência em temperatura ambiente

    # Calcula resistência
    return (fcu_high - fcu_room) / fcu_room