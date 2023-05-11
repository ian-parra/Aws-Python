renta = float(input("Ingrese su renta anual en euros: "))

tramos_impositivos = [(10000, 0.05), (20000, 0.15), (35000, 0.20), (60000, 0.30), (float('inf'), 0.45)]

for tramo, tipo_impositivo in tramos_impositivos:
    if renta < tramo:
        print("Su pago impositivo correspondiente es:", tipo_impositivo*100, "%")
        break




