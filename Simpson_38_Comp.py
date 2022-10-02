import numpy as np

def compsim38(a,b,n,f):
    if n%3==0:
        h=(b-a)/n
        suma=f(a)+f(b)
        for i in range(1,n):
            if i%3==0:
                suma+=2*f(a+i*h)
            else:
                suma+=3*f(a+i*h)
        return suma*(3*h/8)
    else:
        return "'n' debe ser múltiplo de 3"

#Funciones f(x)
f1=lambda x: np.exp(x**2)
f2=lambda x: 1 + np.exp(-x)*np.sin(4*x)
f3=lambda x: np.sin(np.pi*x)
f4=lambda x: 1+np.exp(-x)*np.cos(4*x)
f5=lambda x: np.sin(np.sqrt(x))

print(compsim38(0,0.5,99,f1))
print(compsim38(0,1,99,f2))
print(compsim38(0,1,99,f3))
print(compsim38(0,1,99,f4))
print(compsim38(0,1,99,f5))