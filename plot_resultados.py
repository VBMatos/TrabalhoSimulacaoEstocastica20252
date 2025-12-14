import numpy as np
import matplotlib.pyplot as plt

def plot_results(p_resist_tempr, resist_compr, taxa_vol_erosao):
    plt.figure(figsize=(7, 8))
    plt.subplot(3, 1, 1)
    plt.hist(p_resist_tempr, bins=100, color='royalblue')
    plt.title('Distribuição da Perda de Resistência Após Altas Temperaturas')
    plt.xlabel('Perda de Resistência', fontsize=10)
    plt.ylabel('Frequência', fontsize=10)


    plt.subplot(3, 1, 2)
    plt.hist(resist_compr, bins=100, color='salmon')
    plt.title('Distribuição da Resistência à Compressão')
    plt.xlabel('Resistência à Compressão', fontsize=10)
    plt.ylabel('Frequência', fontsize=10)


    media_taxa_erosao = np.mean(taxa_vol_erosao)
    std_taxa_erosao = np.std(taxa_vol_erosao)
    mediana_taxa_erosao = np.median(taxa_vol_erosao)

    plt.subplot(3, 1, 3)
    plt.hist(taxa_vol_erosao, bins=100, color='lightgreen')
    plt.title('Distribuição da Taxa de Erosão')
    plt.xlabel('Taxa de Erosão', fontsize=10)
    plt.ylabel('Frequência', fontsize=10)
    plt.axvline(media_taxa_erosao, color='red', linestyle='dashed', linewidth=2, label='Média')
    plt.axvline(media_taxa_erosao + std_taxa_erosao, color='green', linestyle='dashed', linewidth=2, label='Média + Desvio Padrão')
    plt.axvline(media_taxa_erosao - std_taxa_erosao, color='green', linestyle='dashed', linewidth=2, label='Média - Desvio Padrão')
    plt.axvline(mediana_taxa_erosao, color='purple', linestyle='dashed', linewidth=2, label='Mediana')


    plt.legend()
    plt.tight_layout()
    plt.show()