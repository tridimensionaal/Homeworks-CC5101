from random import randint 
import math
import matplotlib
import matplotlib.pyplot as plt

#Función número armónicos
def Hn(n):
    suma = 0
    for i in range(1,n+1):
        suma += 1/i
    return suma

#Largo baraja
n = 50;
simulaciones = 10000
#Valor pasos cantidad de pasos de las simulaciones
tiempos = []
x = [i for i in range(simulaciones)]

maximo = -1
minimo = 2000

#Valor esperado
Ex = n*Hn(n-1)+1
#Valores para las posiciones de los valores de las simulaciones (respecto a E[X])
diferencias = []

#Simulaciones
for j in range(0,simulaciones):
    i = 0;
    pasos = 0

    while i <n:
        a = randint(0,n)

        if a <= i:
            i += 1
        pasos += 1

    tiempos += [pasos]
    if pasos < minimo:
        minimo = pasos
    if pasos > maximo:
        maximo = pasos


    if pasos < Ex:
        diferencia = -1
    else:
        diferencia = 1
    diferencias += [diferencia]

rango = maximo - minimo

y = [Ex for i in range(simulaciones)]

#Primer gráfico
plt.plot(x,tiempos,'.',label = "F1(n) = Pasos n-ésima simulación")
plt.plot(x,y,'r-', label = "F2(n) = E[X]")
plt.title("Visualización simulaciones en un gráfico xy")
plt.ylabel("Cantidad de pasos")
plt.grid(True)
plt.legend()
plt.show()

#Segundo gráfico
plt.hist(tiempos,rango)
plt.title("Visualización simulaciones en un histograma")
plt.ylabel("Frecuencia")
plt.xlabel("Cantidad de pasos")
plt.xlim(0,maximo)
plt.axvspan(Ex-1, Ex+1, color='red', alpha=0.5)
plt.show()

#Tercer gráfico
plt.hist(diferencias,3)
plt.title("Visualización de la posición de los datos respecto a E[X]")
plt.ylabel("Frecuencia")
plt.xlabel("Posición de los pasos")
plt.xticks([-0.75,0.75], ["Menores a E[X]", "Mayores a E[X]"])
plt.show()





