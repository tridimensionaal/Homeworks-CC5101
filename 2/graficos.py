import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True})

def an(n):
    return 2*( 1 +  n*np.ceil(np.log2(n+1)) - 2**(np.ceil(np.log2(n+1))) + np.ceil(np.log2(n+1))) - n

def bn(n):
    return n*(2 + np.ceil(np.log2(n))) - 2**(np.ceil(np.log2(n)))

def dif(n):
    return 2 + n*np.ceil(np.log2(n+1)) - 2**(np.ceil(np.log2(n+1))) + 2*np.ceil(np.log2(n+1)) - 3*n

n = 100000
a_n = np.zeros(n)
b_n = np.zeros(n)
n_log = np.zeros(n)
log2 = np.zeros(n)
dif_n = np.zeros(n)

for i in range(1,n):
    a_n[i] = an(i)
    b_n[i] = bn(i)
    n_log[i] = i*np.log2(i)
    log2[i] = np.log2(i)
    dif_n[i] = dif(i)

#Gráfico 1
x = np.arange(n)
plt.plot(x,a_n, 'r-', linewidth = 2,label = "$a_{n}$")
plt.plot(x,b_n, 'b-', linewidth = 2, label = "$b_{n}$")
plt.plot(x,n_log, 'g-',linewidth = 1, label = "$n\log_{2}(n)$")
plt.plot(x,log2, 'c-', linewidth = 1,label = "$\log_{2}(n)$")
plt.plot(x,x, 'm-', linewidth = 1, label = "$n$")
plt.title("Comparación variantes búsqueda binaria")
plt.xlabel("n [Largo del arreglo]")
plt.ylabel("c [Número de comparaciones]")
plt.legend()
plt.grid(True)
plt.show()

#Gráfico 2
plt.plot(x,dif_n, 'r-', linewidth = 2,label = "$c_{n}$")
plt.plot(x,n_log, 'g-',linewidth = 1, label = "$n\log_{2}(n)$")
plt.plot(x,log2, 'c-', linewidth = 1,label = "$\log_{2}(n)$")
plt.plot(x,x, 'm-', linewidth = 1, label = "$n$")
plt.title("Visualización $c_{n}$")
plt.xlabel("n [Largo del arreglo]")
plt.ylabel("c [Número de comparaciones]")
plt.legend()
plt.grid(True)
plt.show()
