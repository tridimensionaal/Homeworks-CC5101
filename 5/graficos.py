import numpy as np 
import scipy.special
import matplotlib.pyplot as plt

def Hs(n):
    Hs = np.zeros(n)
    Hs[0] = 1

    for i in range(1,n):
        Hs[i] += (Hs[i-1] + 1/(i+1))

    return Hs

n = int(1e6)

Hns = Hs(n+1)
C1 = np.zeros(n)
C2 = np.zeros(n)
x = np.zeros(n)

for i in range(1,n):
    C1[i] = 2*(Hns[i+1] - 1)
    C2[i] = (12/7)*Hns[i+1] - (10564*i + 6889)/(3920*(i+1))
    x[i] = i

#Latex para matplotlib    
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

#Primer gráfico
plt.plot(x,C1,'-',label = "$C_{n}$")
plt.plot(x,C2,'-',label = "$\hat{C_{n}}$")
plt.title("Comparación costo promedio de búsqueda infructosa")
plt.ylabel("Costo promedio de búsqueda")
plt.xlabel("Cantidad de llaves en el árbol")
plt.grid(True)
plt.legend()
plt.show()

#Segundo gráfico
plt.plot(x,C1 - C2,'r-',label = "$C_{n} - \hat{C_{n}}$")
plt.title("Diferencia costo promedio de búsqueda infructosa")
plt.ylabel("Costo promedio de búsqueda")
plt.xlabel("Cantidad de llaves en el árbol")
plt.grid(True)
plt.legend()
plt.show()

#Segundo gráfico
plt.plot(x,x ,'-',label = "$f(x) = x$")
plt.plot(x,x/2 ,'-',label = "$g(x) = x/2$")
plt.title("Visualización funciones $f(x)$ y $g(x)$")
plt.ylabel("y")
plt.xlabel("x")
plt.grid(True)
plt.legend()
plt.show()









