segundos = float(input("inserta cantidad de segundos: "))

minutos = segundos // 60
horas = segundos // 3600
print("segundos:",segundos,"\nminutos: ",(minutos),"\nhoras: ",(horas))

horas = segundos//3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(horas, minutos, segundos)