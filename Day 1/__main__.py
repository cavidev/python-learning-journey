# Vas a crear un código en Python que le pida a tu amigo que responda dos preguntas que
# requieran una sola palabra cada una y que luego le muestre en pantalla esas palabras
# combinadas, para formar una marca creativa.
# si quieres agregar dificultad al desafío, te sugiero que intentes que el nombre de la
# cerveza se imprima entre comillas. Recuerda que hay diferentes formas de que la función print
# muestre las comillas sin cortar el string, y que ingrese la impresión final en al menos dos líneas
# utilizando saltos de línea dentro del código.

# __main__.py

def main():
    # Los string son cadenas de textos en comillas

    # En este caso, imprime un string, no el resultado de la operacion matematica
    # por que el interprete ve todo como un string
    print('100 + 50')

    # Se pueden concatenar los strings
    print("Hola" + "Carlos")

    # Con la barra \ puede decirle al interprete que sea un caracter especial
    print("Me llamo \"Carlos\"")

    # Se puede imprimir dos lineas con los caracteres especiales
    print("Linea 1\nLinea 2")

    # Se puede agregar la tabulacion
    print("Linea sin tabulacion\n\tTiene una tabulacion")

    print("Iniciando la aplicación desde el paquete")
    print("Hola, hoy te voy a ayudar a escoger un numbre para tu cerveza")
    print("Solo conteste estas simples preguntas: ")
    print("Tu cerveza llevaria el nombre de:\n\""
          + input("Si tuvieras un gato, de color amarillos como se llamaria?: ") + " "
          + input("Escoge el nombre de una ciudad del mundo: ")+"\"")


if __name__ == "__main__":
    main()
