alumnos= eval(input("cuantos alumnos asistiran al viaje?"))
if alumnos < 50:
    if alumnos < 30:
        precio_alumno = 4000 / alumnos
        costo_viaje = 4000
    else:
        precio_alumno = 95
        costo_viaje = alumnos * 95
else:
    if alumnos > 100:
        precio_alumno = 65
        costo_viaje = alumnos * 65
    else:
        precio_alumno = 70
        costo_viaje = alumnos * 70
print("El precio que se pagara por alumno es de: ",round(precio_alumno,2),"\nEl costo total del viaje es de: ",costo_viaje)