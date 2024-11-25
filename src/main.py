import pandas as pd
from analise import calcular_estatisticas
from visualizacao import plotar_histograma


def main():
    # Carregar dados
    df = pd.read_csv('../data/notas.csv')

    # Calcular estatísticas
    media, mediana, variancia, desvio_padrao = calcular_estatisticas(df)

    # Exibir resultados
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Variância: {variancia:.2f}')
    print(f'Desvio Padrão: {desvio_padrao:.2f}')

    # Plotar histograma
    plotar_histograma(df)


if __name__ == '__main__':
    main()
