"""Muestra todos los números primos entre 1 y 250.
Almacene los resultados en un archivo results.txt .
Pruebe el script. Compruebe que produjo los resultados esperados en el archivo results.txt ."""


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Guardar números primos en un archivo de texto
with open("results.txt", "w") as archivo:
    for numero in range(1, 251):
        if es_primo(numero):
            archivo.write(str(numero) + "\n")
