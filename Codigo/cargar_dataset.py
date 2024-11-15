import pandas as pd

# Define la ruta del archivo CSV
ruta_dataset = r"C:\Users\JONANNA\Documents\MINE\codigo_cirrosis\cirrhosis.csv"

# Carga los datos desde el archivo CSV usando la ruta definida en la parte superior, que hace referencia a repositorio en PC
data = pd.read_csv(ruta_dataset)

# Muestra las primeras filas y la información básica del DataFrame
print(data.head())
print(data.info())
