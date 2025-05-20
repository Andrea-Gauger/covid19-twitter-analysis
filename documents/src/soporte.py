# Tratamiento de datos
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
from scipy.stats import shapiro, kstest

import re

# Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

def apertura_exploracion(csv):

    """ Función para leer csv, convertir a df y hacer una primera exploración."""
    
    try:
        # Convertir el csv a DataFrame
        df = pd.read_csv(f"../files/{csv}.csv")        

        # Muestro las primeras filas
        display(df.head())

        # Obtengo las listas
        print(f"-----\n\nEl DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n-----")

        # Consulto si hay filas duplicadas
        print(f"\nEl número de filas duplicadas es {df.duplicated().sum()}\n-----")

        # Muestro el tipo de dato y si hay nulos por cada columna
        print("\nInformación del DataFrame:")
        df.info()

        # Muestro las estadísticas de columnas numéricas
        print("-----\n\nEstadísticas descriptivas:")
        display(df.describe().T)

        # Muestro las estadísticas de columnas no numéricas
        print("-----\n\nEstadísticas objetos:")
        display(df.describe(include="O").T)

        # Me devuelve un df que tendré que igualar a una variable
        return df  

    # Excepciones en caso de no enconrar el archivo o de que haya un error
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '../files/{csv}.csv'.")
        return None  
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None 