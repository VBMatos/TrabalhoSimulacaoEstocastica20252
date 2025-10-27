import numpy as np

def calcular_entropia(presist, rcomp, k):
    # if rcomp == 0:
    #     raise ValueError("Rcomp não pode ser zero.")

    return k * np.abs(presist) / rcomp