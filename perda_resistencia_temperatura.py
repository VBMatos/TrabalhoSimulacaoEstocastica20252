def perda_resist_temp(n_sim, rng):

    fcu_high_mean, fcu_high_std = 50, 2 # MPa
    fcu_room_mean, fcu_room_std = 60, 3 # MPa

    # Amostras aleatórias
    fcu_high = rng.normal(fcu_high_mean, fcu_high_std, n_sim) # Média da resistência após altas temperaturas
    fcu_room = rng.normal(fcu_room_mean, fcu_room_std, n_sim) # Média da resistência em temperatura ambiente

    # Calcula resistência
    return (fcu_high - fcu_room) / fcu_room