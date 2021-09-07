#COMPARAMOS LA VELOCIDAD DE OPERACIONES USANDO NP.ARRAY VS PYTHON LIST
#Mucho más rápido trabajar con arrays
#Iniciamos con 2 lists y a la 2da la tratamos como array

import numpy as np
from timeit import default_timer as timer

# randn devuelve una distribución normal gaussiana
a= np.random.randn(1000)
b= np.random.randn(1000)

A=list(a)
B=list(b)

T=1000

def dot1(): #uso python list
    dot=0
    for i in range(len(A)):
        dot += A[i]*B[i] # multiplica cada elemento de una list x cada elemento de otra list
    return dot

def dot2(): #uso np.array
    return np.dot(a,b) # dot product is an operation that takes two equal arrays and returns a single number
# en este caso a y b son 2 arrays de 1D, asique obtengo un escalar como resultado

start= timer()
for t in range(T):
    dot1()
end= timer()
t1= end-start

start= timer()
for t in range(T):
    dot2()
end= timer()
t2= end-start

print('list calculation: ', t1)
print('np.dot: ', t2)
print('ratio: ', t1/t2)
