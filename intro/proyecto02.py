nombre = input("por favor diga su nombre: ")

ventas = int(input("diga sus ventas totales: "))

comision = round(ventas * 13 / 100, 2)

print(f"Hola! {nombre} el total de comisiones de este mes es: ${comision}")
