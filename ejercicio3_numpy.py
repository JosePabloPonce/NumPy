#Jose Pablo Ponce 19092
#20-03-19
#ejercicio2_numpy
#Ejercicio que muestra la cantidad de juguetes femeninos, de hombres y genericos y la grafica de juguetes contra tiempo


import numpy as np
import matplotlib.pyplot as plt # imporar las funciones para graficar

matriz1= np.mat ([[1/3, 1/6, 2/3], [1/6, 2/3, 1/3],[1.05,-1,0]]) #Crear matriz de ecuaciones
resultado= np.mat ([[756], [1260],[0]]) # Crear matriz con los tiempos igualados
matrizinv= matriz1.I #Crear nueva variable de matriz invertida

r= matrizinv * resultado #Realizar la operacion de la matriz invertida y los resultados
print(r) #Mostrar en pantalla


#asignar coeficientes por medio de la respuestas definida como "r"
masculino1 = r[0,0] 
femenino1 = r[1,0]
generico1 = r[2,0]

#asignar tamaño a las lineas
x = np.array([0,1440])
y1 = np.array([0,masculino1])
y2 = np.array([0,femenino1])
y3 = np.array([0,generico1])

#aasignar color a las lineas  yleyenda
femenino = plt.plot(x, y2, color = "orange", label="Femenino")
masculino = plt.plot(x, y1, color= "blue",label="Masculino")
generico = plt.plot(x, y3, color= "red", label="Genericos")

#nombrar titulo de grafica
plt.title("Jugetes contra tiempo")

#Asignar a X y Y que es cada una
plt.xlabel("Tiempo en min.")
plt.ylabel("Juguetes")
#Mostrar leyenda y cuadricula
plt.legend()
plt.grid()
#mostrar en pantalla
plt.show()
