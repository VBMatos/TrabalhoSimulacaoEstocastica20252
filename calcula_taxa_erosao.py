def calcula_taxa_erosao(resist_compr, n_sim, rng):
    # Parâmetros
    media_peso_antes = 1000
    desvio_peso_antes = 10

    media_peso_depois = 950
    desvio_peso_depois = 10

    media_densidade = 1.0
    desvio_densidade = 0.02


    # Distribuição Normal do peso do refratário antes do uso
    distr_peso_antes = rng.normal(media_peso_antes, desvio_peso_antes, n_sim)

    # Distribuição Normal do peso do refratário após o uso
    distr_peso_depois = rng.normal(media_peso_depois, desvio_peso_depois, n_sim)

    # Distribuição Normal da densidade geométrica do refratário
    distr_densidade = rng.normal(media_densidade, desvio_densidade, n_sim)


    # Calcula taxa
    return ((distr_peso_antes - distr_peso_depois) / distr_densidade) - resist_compr