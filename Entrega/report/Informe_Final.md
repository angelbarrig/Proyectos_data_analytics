Análisis del Dataset de Marketing Bancario
1. Introducción
En este proyecto hemos trabajado con un dataset de campañas de marketing de un banco. La idea es entender qué cosas influyen en que un cliente diga “sí” a abrir un depósito y ver si podemos entrenar modelos que lo predigan.

El trabajo se ha dividido en tres partes:

limpiar los datos,

explorarlos para ver qué patrones tienen,

y entrenar modelos para ver si podemos predecir la respuesta.

Este documento resume lo que hemos ido encontrando.

2. Descripción del dataset
El dataset viene del repositorio UCI y contiene información de clientes, campañas anteriores, duración de llamadas, tipo de contacto y algunos indicadores económicos.

La variable que queremos predecir es:

Código
y → yes / no (si el cliente aceptó el depósito)
Tiene unas 41.000 filas y 21 columnas.
Es un problema de clasificación binaria.

3. Limpieza y transformación (Notebook 1)
En la parte de limpieza hicimos lo básico para dejar el dataset listo:

Revisamos si había valores nulos (prácticamente no había).

Ajustamos tipos de datos para que las columnas estuvieran bien definidas.

Convertimos las variables categóricas a formato adecuado para modelar.

Pasamos la variable objetivo de “yes/no” a 1 y 0.

Guardamos el dataset limpio en Data/Processed.

Con esto ya teníamos un archivo preparado para el EDA y el modelado.

4. Análisis Exploratorio (Notebook 2)
Aquí nos dedicamos a mirar los datos con gráficos y estadísticas sencillas.

Distribuciones
La mayoría de clientes tienen entre 30 y 50 años.
La duración de las llamadas está muy desbalanceada: muchas llamadas cortas y pocas largas.

Outliers
Hay valores extremos en la duración de llamadas y en el número de contactos previos.

Correlaciones
La variable que más relación tiene con el “sí” es la duración de la llamada.
Las variables económicas apenas aportan correlación.
Cuantas más veces se contacta a un cliente, menos probable es que diga “sí”.

Relación con la variable objetivo
Lo más importante que vimos es:

Las llamadas largas suelen acabar en “sí”.

Llamar muchas veces al mismo cliente no funciona bien.

Si el cliente tuvo una experiencia positiva en campañas anteriores, es más probable que acepte.

5. Modelado (Notebook 3)
Probamos varios modelos para ver cuál predice mejor la respuesta del cliente.

Modelos usados
Regresión Logística

Random Forest

Gradient Boosting

(Opcional) XGBoost si está disponible

Métricas
Miramos accuracy, precision, recall, F1 y ROC AUC.

Resultados
Los modelos basados en árboles (Random Forest y Gradient Boosting) funcionan mejor que la regresión logística.
La regresión logística sirve como punto de partida, pero los modelos más complejos captan mejor los patrones.

Matriz de confusión
Los modelos aciertan mucho los “no”, pero les cuesta más acertar los “sí”, porque hay muchos más “no” en el dataset.

Importancia de variables
Las variables más importantes fueron:

duration

nr.employed

cons.price.idx

campaign

pdays

6. Conclusiones
La duración de la llamada es la variable clave.

Llamar demasiadas veces a un cliente no ayuda.

Los modelos de árboles funcionan mejor que la regresión logística.

El desbalance del dataset hace que los modelos tengan más dificultad con los “sí”.

7. Limitaciones
El dataset está desbalanceado (muchos “no”, pocos “sí”).

Algunas variables económicas aportan poca información.

La variable duration solo se conoce después de la llamada, así que no sirve para predecir antes de contactar.