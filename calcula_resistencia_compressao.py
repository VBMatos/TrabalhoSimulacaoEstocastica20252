import numpy as np
from scipy.stats import truncnorm

def calcula_resist_compres(p_resist_tempr, n_sim, rng):
    # Parâmetros
    media_carga_ruptura = 20000
    desvio_carga_ruptura = 1000

    # Distribuição Normal da carga de ruptura
    a, b = (0 - media_carga_ruptura) / desvio_carga_ruptura, np.inf
    distr_carga_ruptura = truncnorm(a, b, loc=media_carga_ruptura, scale=desvio_carga_ruptura)
    distr_carga_ruptura = distr_carga_ruptura.rvs(n_sim)

    media_area_refratario = 170

    # Calcula resistência
    res_base = distr_carga_ruptura / media_area_refratario

    return res_base - (res_base * p_resist_tempr)