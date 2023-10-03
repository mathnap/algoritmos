"""muestre el promedio redondeado hacia arriba dado con 3 calificaciones"""
import math

calificacion1 = int(input("calificacion 1: "))
calificacion2 = int(input("calificacion 2: "))
calificacion3 = int(input("calificacion 3: "))

promedio = (calificacion1 + calificacion2 + calificacion3)/3

print("promedio sin redondeo:",promedio)
print("promedio con redondeo hacia arriba:",math.ceil(promedio))
print("promedio con redondeo hacia abajo:",math.floor(promedio))
print("promedio con redondeo normal: ",round(promedio))