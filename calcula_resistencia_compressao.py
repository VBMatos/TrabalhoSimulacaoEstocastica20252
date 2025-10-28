def calcula_resist_compres(Presist_temp, n_sim, rng):

    P_mean, P_std = 20000, 500    # N
    A_mean, A_std = 0.005, 0.0001 # m²

    # Amostras aleatórias
    fcu_carga = rng.normal(P_mean, P_std, n_sim) # Média da carga de ruptura
    fcu_area = rng.normal(A_mean, A_std, n_sim) # Média da área do refratário

    # Calcula resistência
    return (fcu_carga / fcu_area) - Presist_temp