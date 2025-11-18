import numpy as np

def log_results(p_resist_tempr, resist_compr, taxa_vol_erosao):
    print("----------------------------------------------")
    print("Resumo estatístico da perda_resist:")
    print(f"Média: {np.mean(p_resist_tempr):.2f}")
    print(f"Mediana: {np.median(p_resist_tempr):.2f}")
    print(f"Desvio padrão: {np.std(p_resist_tempr):.2f}")
    print(f"Mínimo: {np.min(p_resist_tempr):.2f}, Máximo: {np.max(p_resist_tempr):.2f}")
    print("----------------------------------------------")

