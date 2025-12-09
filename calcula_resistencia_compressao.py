import numpy as np
from scipy.stats import truncnorm

def calcula_resist_compres(p_resist_tempr, n_sim, rng):
    # Parâmetros
    media_carga_ruptura = 20000 #(N)
    desvio_carga_ruptura = 1000 #(N)

    # Limites de truncagem
    limite_min = 19000 #(N)
    limite_max = 21000 #(N)

    # Distribuição Normal da carga de ruptura
    a = (limite_min - media_carga_ruptura) / desvio_carga_ruptura
    b = (limite_max - media_carga_ruptura) / desvio_carga_ruptura

    distr_carga_ruptura = truncnorm(a, b, loc=media_carga_ruptura, scale=desvio_carga_ruptura)
    distr_carga_ruptura = distr_carga_ruptura.rvs(n_sim) #rvs: Gerador de variáveis aleatórias com base em uma probabilidade pré-definida

    media_area_refratario = 170 #(cm³)

    # Calcula resistência
    res_base = distr_carga_ruptura / media_area_refratario

    return res_base - (res_base * p_resist_tempr)