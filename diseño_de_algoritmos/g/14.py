print("cuantas personas habra en la cena?")
personas=eval(input())
if personas <= 300:
    if personas <= 200:
        banquete = personas*95
        print(personas*95, "es el costo total")
    else:
        banquete = personas*85
        print(personas*85, "es el costo total")


else:
    if personas >= 300:
        banquete = personas*75
        print(personas*75, "es el costo total")
print("el costo del banquete por", personas, "es de: ", banquete)