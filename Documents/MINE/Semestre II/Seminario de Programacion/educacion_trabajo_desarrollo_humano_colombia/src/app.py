import streamlit as st
import pandas as pd
import sys
import os

# Aseg�rate de que Python reconozca la carpeta models
sys.path.append(os.path.join('C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\src\\models'))

# Importar la funci�n de entrenamiento del modelo
from modelo_regresion import entrenar_modelo

# T�tulo de la aplicaci�n
st.title("An�lisis de Datos de Educaci�n para el Trabajo y el Desarrollo Humano en Colombia")

# Definir la ruta del archivo de Excel
ruta_datos = "C:\\Users\\djsol\\Documents\\MINE\\Semestre II\\Seminario de Programacion\\educacion_trabajo_desarrollo_humano_colombia\\data.xlsx"

# Cargar los datos desde cada hoja con openpyxl
@st.cache_data  # Uso de la cach� para mejorar el rendimiento
def cargar_datos_excel(ruta):
    try:
        data = pd.read_excel(ruta, sheet_name=None, engine='openpyxl')
        return data
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

# Cargar los datos desde el archivo de Excel
data = cargar_datos_excel(ruta_datos)

if data:
    # Selecci�n de la hoja
    sheet_name = st.selectbox("Selecciona una hoja:", options=data.keys())
    df = data[sheet_name]

    # Mostrar los datos de la hoja seleccionada
    st.write(f"Datos de la hoja: {sheet_name}")
    st.write(df)

    # Bot�n para entrenar el modelo
    if st.button("Entrenar Modelo de Regresi�n Log�stica"):
        accuracy = entrenar_modelo()
        st.success(f"El modelo se ha entrenado con una precisi�n del {accuracy:.2%}")
