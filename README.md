
# Proyecto para clasificación inicial de las etapas de la cirrosis

## Descripción
Análisis de datos de pacientes con cirrosis, con preprocesamiento y modelos de clasificación para predecir el estado del paciente. Este modelo puede servir como una primera aproximación para entender qué variables y patrones pueden estar asociados con diferentes etapas de la cirrosis.

El proceso para crear el repositorio y ejecutar el proyecto codigo_cirrosis comenzó con la creación del repositorio en GitHub. Se clonó el repositorio vacío utilizando el comando git clone https://github.com/SP2024MINE/codigo_cirrosis.git en el directorio local. 

Posteriormente, se verificó la configuración de Git en el sistema y se resolvieron problemas de permisos para garantizar que Git tuviera acceso adecuado  a los archivos. Se configuró correctamente el archivo .gitignore para evitar que archivos temporales y no relevantes fueran subidos al repositorio. Una vez configurado el repositorio, se instalaron las dependencias necesarias, comenzando con la creación de un entorno virtual con conda o pip. A continuación, se ejecutaron los comandos correspondientes para instalar bibliotecas como pandas, numpy y otras necesarias para el proyecto. Al enfrentar problemas con el entorno, se resolvieron algunos errores de importación de librerías, y se verificó que las dependencias estuvieran instaladas correctamente. Para ejecutar el proyecto, se inició el proceso de exploración de datos, en el que se cargaron los datos relevantes del archivo CSV y se realizó un análisis preliminar de la estructura de los datos. Se identificaron los valores nulos en las columnas importantes, como la columna 'Stage', y se imputaron utilizando métodos apropiados, como el reemplazo por el valor más frecuente. Se pasó luego al preprocesamiento de los datos, limpiando las entradas y normalizando variables si era necesario. 

## Estructura del Proyecto
- `entrenamiento_modeloV4.ipynb`: Notebook de entrenamiento del modelo.
- `preprocesador_cargado.ipynb`: Notebook para cargar el preprocesador.
- `cirrhosis.csv`: Dataset utilizado para el análisis.
- `Codigo/`: Carpeta que contiene todos los archivos de código y los pipelines guardados en joblib.

## Instrucciones de Uso
### Requisitos previos
1. Instalar Anaconda PowerShell Pront y Visual Studio Code: Esto facilita la creación y gestión de entornos virtuales.
2. Clonar el repositorio: Abre una terminal y ejecuta el siguiente comando
git clone https://github.com/SP2024MINE/codigo_cirrosis.git
3. Entrar en el directorio del proyecto
cd codigo_cirrosis
#### Instalación
1. Crear un entorno virtual: Abre la terminal en la carpeta del proyecto y ejecuta:
2. Instalar las dependencias: Instala las bibliotecas necesarias utilizando pip o conda. Si tienes un archivo requirements.txt
pip install -r requirements.txt
3. Configurar Jupyter Notebook: Si deseas ejecutar el proyecto en Jupyter Notebook, instala Jupyter:
### Ejecución
1. Abrir Jupyter Notebook: Inicia Jupyter Notebook en el directorio del proyecto:
jupyter notebook
Luego, abre el archivo entrenamiento_modeloV4.ipynb.
2. Ejecutar las Celdas: En el notebook, ejecuta cada celda en orden para preprocesar los datos, entrenar el modelo y guardar los pipelines.
3. Cargar y Evaluar el Modelo: Para probar el modelo con datos nuevos, ejecuta las celdas correspondientes en el notebook o en otro script de Python utilizando los pipelines guardados (preprocesamiento_pipeline.joblib y modelo_completo_pipeline.joblib).

## Resultados
El modelo de clasificación Random Forest fue entrenado para predecir la etapa de la enfermedad hepática basándose en el conjunto de datos de cirrosis. A continuación se resumen las métricas de evaluación clave obtenidas:
* Precisión: La clase 1 tiene una precisión de 0.00, lo que indica que el modelo no logró clasificar correctamente ninguna muestra en esta categoría.
La clase 3 tiene una precisión de 0.55, y la clase 4 de 0.65, lo que indica un desempeño más confiable en estas categorías.
* Exactitud (Recall): La clase 3 muestra una exhaustividad alta de 0.76, lo que significa que el modelo es bastante efectivo en identificar esta categoría.
Sin embargo, la clase 1 nuevamente tiene un recall de 0.00, lo que confirma que el modelo no detecta ningún caso en esta categoría.
* Puntaje F1: El F1-score proporciona un equilibrio entre precisión y exhaustividad.
Las clases 3 y 4 presentan F1-scores relativamente altos de 0.64 y 0.60, respectivamente, lo que indica un buen balance en estas clases.
En cambio, las clases 1 y 2 tienen valores de F1 bajos, mostrando que el modelo tiene dificultades para clasificarlas adecuadamente.
* Promedios ponderados y macro:
El macro promedio de precisión, exhaustividad y F1 es bajo (aproximadamente 0.37 para cada métrica), lo que revela un rendimiento moderado en todas las clases sin tener en cuenta el tamaño de cada una.
El promedio ponderado es un poco mejor, especialmente para la precisión y el F1 (0.52 y 0.52), ya que tiene en cuenta el número de muestras en cada clase.

## Interpretación de Resultados
El modelo muestra un buen rendimiento en las clases 3 y 4, mientras que las clases 1 y 2 presentan desafíos en términos de predicción. Estos resultados sugieren que el modelo podría ser útil en un entorno de diagnóstico asistido por computadora, pero se requieren mejoras, particularmente en las clases donde el rendimiento es bajo. En el contexto médico, sería esencial optimizar la capacidad del modelo para todas las clases, dado que una clasificación incorrecta podría tener implicaciones significativas para la salud del paciente.

## Referencias
* Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). "Scikit-learn: Machine Learning in Python." Journal of Machine Learning Research, 12, 2825-2830.

Este artículo describe la biblioteca scikit-learn, que se utilizó para implementar los algoritmos de preprocesamiento y modelos de clasificación en Python.

* Bruce, P., Bruce, A., & Gedeck, P. (2020). Estadística práctica para ciencia de datos con R y Python. Alpha Editorial (Marcombo).

Este libro proporciona una base estadística sólida y una introducción práctica al análisis de datos utilizando Python, lo que respalda las técnicas de preprocesamiento y evaluación de modelos empleadas en este proyecto.

* McFarland, W. (Instructor). (n.d.). Introduction to Git and GitHub [Online course]. Coursera. https://www.coursera.org/learn/introduction-git-github

Este curso ofrece una introducción detallada sobre el uso de Git y GitHub para control de versiones, lo cual fue fundamental para la gestión de versiones de este proyecto.
