import pandas as pd

# Ruta al dataset
ruta_dataset = r"C:\Users\JONANNA\Documents\MINE\codigo_cirrosis\cirrhosis.csv"

# Cargar el dataset
data = pd.read_csv(ruta_dataset)

# Mostrar las primeras filas y la información del dataset
print(data.head())
print(data.info())
