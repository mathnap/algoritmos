A = eval(input("escribe el lado A: "))
B = eval(input("escribe el lado B: "))
C = eval(input("escribe el lado C: "))

if A > B+C or B > A+C or C > A+B:
    print("triangulo no valido")
elif A == B != C or B == C != A or A == C != B:
    print("triangulo isoseles")
elif A == B == C:
    print("triangulo equilatero")
elif A != B != C:
    print("triangulo escaleno")
