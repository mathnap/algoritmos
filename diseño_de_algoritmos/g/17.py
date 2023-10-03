dia = input("dia: ")
tiempo = eval(input("tiempo de llamada: "))
turno = input("turno: ")

if tiempo <= 5:
    subtotal = tiempo * 1
else:
    if tiempo <= 8:
        subtotal = (tiempo-5) * .8 + 5
    else:
        if tiempo <= 10:
            subtotal = (tiempo-8) * .7 + 7.4
        else:
            subtotal = (tiempo-10) * .5 + 8.8
if dia.lower() == "domingo":
    impuesto = subtotal * 0.03
else:
    if turno.lower() == "matutino":
        impuesto = subtotal * 0.15
    else:
        impuesto = subtotal * 0.10
total = subtotal + impuesto
print("el subtotal es : ",subtotal)
print("impuesto: ",round(impuesto,2))
print("total: ",round(total,2))