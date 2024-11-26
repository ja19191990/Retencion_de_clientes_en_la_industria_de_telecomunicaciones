import pandas as pd
import numpy as np
from sklearn.utils import shuffle

# ===============================================================================================================================================================================================#


def snakecase(df, columnas):
    # '''
    # Función que cambia los valores tipo str a minúsculas a partir de columnas de un DataFrame
    # '''
    for columna in columnas:
        df[columna] = df[columna].str.lower()
    return df

# ===============================================================================================================================================================================================#


def unique(df, columnnas):
    # '''
    # Función que permite obtener los valores únicos de columnas específicas de un DataFrame
    # '''
    unique_values = []
    for columna in columnnas:
        unique_values.append(df[columna].unique())
    return unique_values


# ===============================================================================================================================================================================================#


def upsample(features, target, repeat):
    # '''
    # Función para realizar sobremuestreo a partir de datos segmentados en características y objetivo
    # '''
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)

    features_upsampled, target_upsampled = shuffle(
        features_upsampled, target_upsampled, random_state=12345
    )

    return features_upsampled, target_upsampled


# ===============================================================================================================================================================================================#
