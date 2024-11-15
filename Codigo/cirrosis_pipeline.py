from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

numeric_features = ['columna1', 'columna2']
categorical_features = ['columna3']

numeric_transformer = SimpleImputer(strategy='mean')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('classifier', RandomForestClassifier())])

# Entrena el modelo
# model_pipeline.fit(X_train, y_train) # reemplaza con tus datos de entrenamiento

# Guarda el pipeline
dump(preprocessor, 'Codigo/preprocessing_pipeline.joblib')
dump(model_pipeline, 'Codigo/model_pipeline.joblib')
