import math

litros = eval(input("litros producidos: "))
precio_por_galon = eval(input("precio del galon: "))

galon = 3.785
galones = litros / galon
precio_total = galones * precio_por_galon

print("total de galones: ", round(galones,2))
print("precio total:", round(precio_total,2))