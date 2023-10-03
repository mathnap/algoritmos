print("dame 3 numeros: ")
a=eval(input())
b=eval(input())
c=eval(input())
if a > b:
     if a > c:
         print(a," es el mayor")
     else:
         print(c," es el mayor")
else:
     if b > c:
         print(b, "es el mayor")
     else:
         print(c," es el mayor")