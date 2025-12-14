import numpy as np

def log_results(taxa_vol_erosao):
    print("----------------------------------------------")
    print("Resumo estatístico da 'Taxa de Erosão':")
    print(f"Média: {np.mean(taxa_vol_erosao):.2f}")
    print(f"Mediana: {np.median(taxa_vol_erosao):.2f}")
    print(f"Desvio padrão: {np.std(taxa_vol_erosao):.2f}")
    print(f"Mínimo: {np.min(taxa_vol_erosao):.2f} | Máximo: {np.max(taxa_vol_erosao):.2f}")
    print("----------------------------------------------")

