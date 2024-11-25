import pandas as pd


def calcular_estatisticas(df):
    media = df['nota'].mean()
    mediana = df['nota'].median()
    variancia = df['nota'].var()
    desvio_padrao = df['nota'].std()

    return media, mediana, variancia, desvio_padrao
