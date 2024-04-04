import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Carga del dataset
df = pd.read_csv('path_to_your_file.csv')  # Cambia 'path_to_your_file.csv' por la ruta de tu archivo

# Paso 1: Eliminación de outliers
Q1 = df.drop('Outcome', axis=1).quantile(0.25)
Q3 = df.drop('Outcome', axis=1).quantile(0.75)
IQR = Q3 - Q1

df = df[~((df.drop('Outcome', axis=1) < (Q1 - 1.5 * IQR)) | (df.drop('Outcome', axis=1) > (Q3 + 1.5 * IQR))).any(axis=1)]

# Paso 2: Selección de características
# Inicialmente, utilizamos todas las características, pero este paso se puede iterar para mejorar el modelo

# Paso 3: Normalización/Estandarización
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('Outcome', axis=1))

# Preparación de los datos para el entrenamiento
X = scaled_features
y = df['Outcome']

# División en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicialización y entrenamiento del modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predicciones y evaluación
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
