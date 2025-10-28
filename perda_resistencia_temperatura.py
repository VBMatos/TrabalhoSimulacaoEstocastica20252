def perda_resist_temp(n_sim, rng):
    # Parâmetros
    media_resist_alta_tempr = 50
    desvio_resist_alta_tempr = 2

    media_resist_baixa_tempr = 60
    desvio_resist_baixa_tempr = 3


    # Distribuição Normal da resistência após altas temperaturas
    distr_alta_tempr = rng.normal(media_resist_alta_tempr, desvio_resist_alta_tempr, n_sim)

    # Distribuição Normal da resistência em temperatura ambiente
    distr_baixa_tempr = rng.normal(media_resist_baixa_tempr, desvio_resist_baixa_tempr, n_sim)


    # Calcula perda de resistência
    return (distr_alta_tempr - distr_baixa_tempr) / distr_baixa_tempr