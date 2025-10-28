def calcula_taxa_erosao(Presist_temp, Rcomp, n_sim, rng):

    P1_mean, P1_std = 1000, 10               # g
    P2_mean, P2_std = 950, 10                # g
    dma_geom_mean, dma_geom_std = 1.0, 0.02  # adimensional

    # Amostras aleatórias
    fcu_peso_antes = rng.normal(P1_mean, P1_std, n_sim) # Média do peso do refratário antes do ciclo
    fcu_peso_depois = rng.normal(P2_mean, P2_std, n_sim) # Média do peso do refratário após o ciclo
    fcu_densidade = rng.normal(dma_geom_mean, dma_geom_std, n_sim) # Média da densidade geométrica do refratário

    # Calcula taxa
    return ((fcu_peso_antes - fcu_peso_depois) / fcu_densidade) - (Presist_temp * Rcomp)