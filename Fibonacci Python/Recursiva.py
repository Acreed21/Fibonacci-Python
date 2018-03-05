from numpy import *
import matplotlib.pyplot as plt
from time import time
#No Recursivo
a=1
b=0
Arreglo = [1,2,3,4,5,6,7,8,9,10]
while_i = 0
while while_i<10:
    time_inicio = time()
    i=while_i*1
    for i in range((while_i+1)*10000):
        b=b+a
        a=b-a
    time_final=time()
    tiempo_total = time_final - time_inicio
    Arreglo[while_i] = tiempo_total
    while_i+=1
plt.plot(Arreglo)
plt.xlabel('Número')
plt.ylabel('Time (s)')

