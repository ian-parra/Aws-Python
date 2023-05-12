edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("pase gratis")
elif edad >= 4 and edad <= 18:
    print("debe abonar 5$")
else:
    print("debe abonar 10$")