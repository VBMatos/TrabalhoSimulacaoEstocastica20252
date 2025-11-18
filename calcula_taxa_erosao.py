def calcula_taxa_erosao(resist_compr, n_sim, rng):
    # Parâmetros
    media_peso_antes = 460

    media_peso_depois_min = 200
    media_peso_depois_max = 455

    media_densidade = 3.0
    vari_densidade = 0.1

    # Distribuição Uniforme do peso do refratário após o uso
    distr_peso_depois = rng.uniform(media_peso_depois_min, media_peso_depois_max, n_sim)

    # Distribuição Uniforme da densidade geométrica do refratário
    distr_densidade = rng.normal(media_densidade, vari_densidade, n_sim)

    # Calcula taxa
    return ((media_peso_antes - distr_peso_depois) / distr_densidade) - resist_compr