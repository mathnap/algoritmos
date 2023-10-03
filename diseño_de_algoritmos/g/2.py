a=eval(input("ingrese el valor de a: "))
b=eval(input("ingrese la base de la figura : "))
c=eval(input("ingrese el valor de c: "))
r=eval(input("ingrese el radio del circulo: "))
h=eval(input("ingrese la altura de la figura: "))

pi=float=3.1416

print("a=",a,end="\n")
print("b=",b,end="\n")
print("c=",c,end="\n")
print("r=",r,end="\n")
print("pi=",pi,end="\n")
print("h=",h,end="\n")

area_circulo=pi*(r**2)
area_triangulo=(b*h)/2

print("el area de circulo es de:",area_circulo,end="\n")
print("el area del triangulo es de: ",area_triangulo,end="\n")