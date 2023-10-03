tipo_de_uvas = (input("ingrese el tipo de uva, A o B: "))
tamano_de_uvas = eval(input("ingrese el tamaño de uva: "))
catidad_de_uvas = eval(input("ingrese la cantidad en kilos de uvas: "))
precio_inicial = eval(input("ingrese el precio inicial: "))

if tipo_de_uvas == "A" or tipo_de_uvas == "a":
    if tamano_de_uvas == 1:
        precio_inicial += 0.20
    else:
        precio_inicial += 0.30
else:
    if tamano_de_uvas == 1:
        precio_inicial -= 0.30
    else:
        precio_inicial -= 0.50
ganancia = (catidad_de_uvas * precio_inicial)
print("precio inicial: ",round(precio_inicial,2))
print("la ganancia es de: ",round(ganancia,2))