from pathlib import Path


def abrir_leer(ruta):
    archivo = open(ruta, "r")
    print(archivo.read())
    return archivo.read()



