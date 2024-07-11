"""
    Práctica 6: Regresión lineal
    Objetivo: Generar la predicción de datos usando regresión lineal
    Equipo 5
        Castro Cazares Carlos Jahir (Responsable)
        Martinez Resendiz Giovanni Hasid
        Velazquez Aguilar Jaime Isai
    #################################################################
    Python v3.8
    Pandas => pip install pandas
    Matplotlib => pip install matplotlib
    Sklearn => pip install -U scikit-learn
    Seaborn => pip install seaborn
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Leer los datos recopilados sobre los contagios del COVID-19
print('Leyendo el archivo Covid_19_Mexico_Mayo.csv . . .\n')
df = pd.read_csv('Covid_19_Mexico_Mayo.csv')

# Calcular la Regresion Lineal
print('Calculando la Regresion Lineal . . .\n')
lm = LinearRegression()
X = df[['dia']] #variable dependiente
Y = df['contagios'] #variable independiente
lm.fit(X,Y)
Yhat=lm.predict(X) #Yhat = contagios

#Calcular la ecuación de la recta y = mx + b
b = lm.intercept_
m = lm.coef_

#Calcular por medio del método de regresión lineal la cantidad de contagios para el día 30 de mayo del 2021.
contagios30 = m*30 + b
print("Los contagios estimados para el 30 de mayo son: ", int(contagios30[0]), '\n')
df = df.append({'fecha': '30/05/2021', 'contagios':int(contagios30[0]), 'dia':30}, ignore_index=True)

# Graficar
plt.figure(figsize=(8, 6))
plt.title("Gráfica de contagios del mes de mayo en México")
sns.regplot(x="dia", y="contagios", data=df)
plt.plot(30, int(contagios30[0]), marker="o", color="red")
plt.ylim(0,)
plt.show()
