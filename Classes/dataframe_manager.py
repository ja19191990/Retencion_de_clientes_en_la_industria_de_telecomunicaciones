# Clase para leer dataframes requeridos sin recurrir a variables globales

import os
import pandas as pd


class DataFrameManager:
    def __init__(self):
        # Diccionario para almacenar los DataFrames
        self.dataframes = {}

    def read_dataframe(self, dataframe_name, folder='Data', subfolder='.ipynb_checkpoints'):
        '''
        Carga un DataFrame desde un archivo CSV y lo guarda en el administrador.

        Args:
        - dataframe_name: nombre base del DataFrame y su diccionario, sin extensión, como string
        - folder: carpeta en donde se encuentra el DataFrame, como string
        - subfolder: subcarpeta en donde se encuentra el DataFrame, como string

        Returns:
        - None. El DataFrame queda almacenado en el administrador.
        '''
        # Ruta del archivo CSV
        file_path = os.path.join(folder, subfolder, f'{dataframe_name}.csv')

        # Importar dinámicamente el diccionario asociado al DataFrame
        dict_module_name = f'Dict.dict_{dataframe_name}'
        dict_module = __import__(dict_module_name, fromlist=[
                                 f'dict_{dataframe_name}'])
        dtype_dict = getattr(dict_module, f'dict_{dataframe_name}')

        # Leer el CSV usando el diccionario de tipos
        self.dataframes[dataframe_name] = pd.read_csv(
            file_path, dtype=dtype_dict)

        print(
            f"DataFrame '{dataframe_name}' cargado exitosamente en el administrador.")

    def get_dataframe(self, dataframe_name):
        '''
        Obtiene un DataFrame cargado previamente.

        Args:
        - dataframe_name: nombre del DataFrame, como string.

        Returns:
        - DataFrame correspondiente al nombre dado.
        '''
        return self.dataframes.get(dataframe_name, None)

    def list_dataframes(self):
        '''
        Lista los nombres de los DataFrames cargados en el administrador.

        Returns:
        - Lista de nombres de los DataFrames.
        '''
        return list(self.dataframes.keys())

    def load_multiple(self, dataframe_names, folder='Data', subfolder='.ipynb_checkpoints'):
        '''
        Carga múltiples DataFrames desde archivos CSV.

        Args:
        - dataframe_names: lista de nombres base de los DataFrames, sin extensión.
        - folder: carpeta en donde se encuentran los DataFrames, como string.
        - subfolder: subcarpeta en donde se encuentran los DataFrames, como string.

        Returns:
        - None. Los DataFrames quedan almacenados en el administrador.
        '''
        for name in dataframe_names:
            self.read_dataframe(name, folder, subfolder)
