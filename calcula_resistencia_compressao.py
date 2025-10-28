def calcula_resist_compres(p_resist_tempr, n_sim, rng):
    # Parâmetros
    media_carga_ruptura = 20000
    desvio_carga_ruptura = 500

    media_area_refratario = 0.005
    desvio_area_refratario = 0.0001


    # Distribuição Normal da carga de ruptura
    distr_carga_ruptura = rng.normal(media_carga_ruptura, desvio_carga_ruptura, n_sim)

    # Distribuição Normal da área do refratário
    distr_area_refratario = rng.normal(media_area_refratario, desvio_area_refratario, n_sim)


    # Calcula resistência
    return (distr_carga_ruptura / distr_area_refratario) - p_resist_tempr