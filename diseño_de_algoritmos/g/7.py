import math

x1 = float(input("X1: "))
x2 = float(input("X2: "))
y1 = float(input("Y1: "))
y2 = float(input("y2: "))

d = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

print("distancia: ",round(d,4))
