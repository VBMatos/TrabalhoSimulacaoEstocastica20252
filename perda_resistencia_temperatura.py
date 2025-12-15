def perda_resist_temp(n_sim, rng):

    # Distribuição uniforme, considerando que a resistência em temperatura
    # ambiente pode variar entre A e B (máxima entropia dado o intervalo) (MPa)
    res_room_temperature = rng.uniform(40, 65, n_sim) #(MPa)

    # Para cada valor de res_room_temperature, sorteia-se uniformemente,
    # considerando que a resistência pode variar entre R e C
    perda_prop = rng.beta(0.3, 0.8, n_sim)
    res_high_temperature = res_room_temperature * (1 - perda_prop)

    # Calcula perda proporcional de resistência (%)
    perda_resist = (res_room_temperature - res_high_temperature) / res_room_temperature

    return perda_resist