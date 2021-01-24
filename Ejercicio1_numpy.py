#Jose Pablo Ponce 19092
#20-3-19
#Ejercicio1_numpy
#Grafica que muestra los datos de ingenieria

import numpy as np # importar Numpy para trabajar con arreglos rápidos
import matplotlib.pyplot as plt # importar las funciones para graficar
x = np.arange(-3.14, 3.14, 0.01) # crear datos para x
y = np.sin(x) # calcular los valores de y
plt.grid() # Mostrar cuadricula de la grafica
plt.title('Gráfica') # Mostrar el titulo
plt.plot(x, y, label='seno de X') # crear la gráfica

plt.legend(loc ='upper left') # mostrar la leyenda de la grafica

plt.show() # mostrar la grafica
