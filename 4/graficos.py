import numpy as np 
import scipy.special
import matplotlib.pyplot as plt

def G(k,p):
    q = 1-p
    prob = 0
    for i in range(0,k-1):
        prob += (scipy.special.comb(k-1+i,i)*p**(k)*q**(i))
    prob += scipy.special.comb(2*(k-1),(k-1))*p**(k-1)*q**(k-1)*((p*p)/(1-2*p*q))
    return prob

def S(p):
    p_g_4 = G(4,p)
    q_g_4 = 1 -p_g_4
    p_g_7 = G(7,p)

    prob = 0
    p_e_6 = p_g_4**6
    for i in range(0,5):
        prob += (scipy.special.comb(5+i,i)*p_e_6*q_g_4**(i))
    prob += (scipy.special.comb(10,5)*p_g_4**(5)*q_g_4**(5)*(p_g_4**2 + 2*p_g_4*q_g_4*p_g_7))
    return prob

def L(p):
    p_g_4 = G(4,p)
    q_g_4 = 1 -p_g_4

    prob = 0
    p_e_6 = p_g_4**6
    for i in range(0,5):
        prob += (scipy.special.comb(5+i,i)*p_e_6*q_g_4**(i))
    prob += (scipy.special.comb(10,5)*p_g_4**(5)*q_g_4**(5)*(p_g_4**2/(1 - 2*p_g_4*q_g_4))) 
    return prob

#Derivada discreta centrada para Gk(p)
def D_G(k,p,h):
    return ((G(k,p+h) - G(k,p-h))/(2*h))

#Derivada discreta centrada para S(p)
def D_S(p,h):
    return ((S(p+h) - S(p-h))/(2*h))

#Derivada discreta centrada para L(p)
def D_L(p,h):
    return ((L(p+h) - L(p-h))/(2*h))


P = []
G_4 = []
G_7 = []
S_l = []
L_l = []

n = int(1e4)
for i in range(0,n+1):
    p = i/n
    P += [p]
    G_4 += [G(4,p)]
    G_7 += [G(7,p)]
    S_l += [S(p)]
    L_l += [L(p)]

#Latex para matplotlib    
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

#Primer gráfico
plt.plot(P,G_4,'-',label = "$G_{4}(p)$")
plt.plot(P,G_7,'-',label = "$G_{7}(p)$")
plt.plot(P,S_l,'-',label = "$S(p)$")
plt.plot(P,L_l,'-',label = "$L(p)$")
plt.title("Visualización funciones $G_{4}(p)$, $G_{7}(p)$, $S(p)$ y $L(p)$")
plt.ylabel("Probabilidad de ganar")
plt.xlabel("Probabilidad que A gane una pelota")
plt.grid(True)
plt.legend()
plt.show()

D_P = []
D_G_4 = []
D_G_7 = []
D_S_l = []
D_L_l = []

h = 1/(n+1)

for i in range(1,n+1):
    p = i/n
    D_P += [p]
    D_G_4 += [D_G(4,p,h)]
    D_G_7 += [D_G(7,p,h)]
    D_S_l += [D_S(p,h)]
    D_L_l += [D_L(p,h)]

#Segundo gráfico
plt.plot(D_P,D_G_4,'-',label = "$G_{4}'(p)$")
plt.plot(D_P,D_G_7,'-',label = "$G_{7}'(p)$")
plt.plot(D_P,D_S_l,'-',label = "$S'(p)$")
plt.plot(D_P,D_L_l,'-',label = "$L'(p)$")
plt.title("Visualización funciones $G_{4}'(p)$, $G_{7}'(p)$, $S'(p)$ y $L'(p)$")
plt.ylabel("Variación de la probabilidad de ganar respecto a la variación $p$")
plt.xlabel("Probabilidad que A gane una pelota")
plt.grid(True)
plt.legend()
plt.show()




