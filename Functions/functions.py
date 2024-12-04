import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import os

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

def save_dataframe(dataframe, name, folder='Data', subfolder='.ipynb_checkpoints'):
    '''
    Función para guardar dataframes en la carpeta indicada en formato .csv

    Args:
    - dataframe: seleccionar aquel a guardar
    - name: nombre del archivo sin extensión .csv, es un string
    - folder: carpeta en dónde se guardará el dataframe, es un string
    - subfolder: subcarpeta en dónde se guardará el dataframe, es un string
    '''
    # Ruta del archivo
    file_path = os.path.join(folder, subfolder, f'{name}.csv')

    # Guardar el DataFrame en formato .csv
    dataframe.to_csv(f'{file_path}', index=False)

    print(f'DataFrame guardado exitosamente en {file_path}')

# ===============================================================================================================================================================================================#


def create_dict(data, name):
    '''
    Función para crear un diccionario donde las claves son las columnas de un DataFrame
    y los valores son los tipos de datos (dtypes) de cada columna. Si es una Series, 
    se usará su nombre como clave y su tipo de dato como valor.

    Args:
    - data: DataFrame o Series de pandas
    - name: Nombre que se usará como base para el diccionario, es un string

    Returns:
    - Un diccionario Python
    '''
    if isinstance(data, pd.DataFrame):
        # Crear el diccionario con las columnas como claves y los tipos de datos como valores
        column_dict = {col: str(dtype)
                       for col, dtype in zip(data.columns, data.dtypes)}
    elif isinstance(data, pd.Series):
        # Crear el diccionario con el nombre de la Series como clave y su tipo de dato como valor
        column_dict = {data.name: str(data.dtype)}
    else:
        raise TypeError(
            "El objeto data debe ser un DataFrame o una Series de pandas.")

    return column_dict


# ===============================================================================================================================================================================================#


def create_and_save_dict(data, name, folder='Dict'):
    '''
    Crea un diccionario basado en un DataFrame o Series, y lo guarda como un archivo .py.

    Args:
    - data: DataFrame o Series de pandas del que se generará el diccionario.
    - name: El nombre del archivo (sin extensión .py) y del diccionario base, es un string.
    - folder: La carpeta donde se guardará el archivo (por defecto: 'Dict'), es un string.
    '''
    # Crear el diccionario usando la función create_dict
    column_dict = create_dict(data, name)

    # Asegurarse de que la carpeta existe
    os.makedirs(folder, exist_ok=True)

    # Crear la ruta completa del archivo
    file_path = os.path.join(folder, f'dict_{name}.py')

    # Escribir el diccionario en el archivo como código Python
    with open(file_path, 'w') as file:
        file.write(f"# Diccionario generado automáticamente para {name}\n")
        file.write(f"dict_{name} = {column_dict}\n")

    print(f"Diccionario generado y guardado exitosamente en: {file_path}")


# ===============================================================================================================================================================================================#
