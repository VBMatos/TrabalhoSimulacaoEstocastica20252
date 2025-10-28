import numpy as np

def perda_resist_compres(sigma_carga, sigma_area, presist_temp, n_sim):

    # Amostras aleatórias
    fcu_carga = np.random.normal(100, sigma_carga, n_sim) # Média da carga de ruptura
    fcu_area = np.random.normal(100, sigma_area, n_sim) # Média da área do refratário

    # Calcula resistência
    return (fcu_carga / fcu_area) - presist_temp