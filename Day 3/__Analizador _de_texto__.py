def countLetters(text, letters):
    """
    Primero: 
        ¿Cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
    recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
    que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
    debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
    y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
    encuentren absolutamente todas las letras es pasar, tanto el texto original como las
    letras a buscar, a minúsculas.
    """
    capitalize = text.upper()
    for letter in letters:
        print(f"La letra {letter} aparece :{capitalize.count(letter.upper())}")


def customeLenght(text):
    """
    Segundo: 
        Le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
    para lograr esta parte, recuerda que hay un método de string que permite transformarlo
    en una lista y que luego hay una función que permite averiguar el largo de una lista.
    """
    print(f"El tamaño del texto que ingresaste es de: {len(list(text))}")


def first_and_later(text):
    """
    Tercero: 
            Nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
    claramente echaremos mano de la indexación.
    """
    print(
        f"La primer letra del texto es: [{text[0]}] y la ultima [{text[-1]}]")


def reverse(text):
    """
    Cuarto: 
        El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
    las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
    que permita unir esos elementos con espacios intermedios? Piénsalo.
    """
    print("El texto invertido se ve de esta manera: ")
    print(" ".join(text[::-1]))


def fountPython(text):
    """
    Quinto: 
        El sistema nos va a decir si la palabra “Python” se encuentra dentro del
    texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
    puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
    manera de expresarle al usuario tu respuesta.
    """
    wasPythonFound = "Python" in text
    dic = {True: "Si", False: "No"}
    print(f"La palabra Python esta en el text? {dic[wasPythonFound]}")
    print()


# __init__
canBe = ["\n\tun artículo entero", "\n\tun párrafo",
         "\n\tuna frase", "\n\tun poema"]
# userText = input(f"Dijite su texto preferido: {''.join(canBe)}\n:: ")
userText = "En un campo de trigo, baila la brisa suave. Flores danzan libres"
# userLetters = input("Ahora ingresa tres letras de tu eleccion:: ").split(" ")
userLetters = ["a", "b", "l"]

print("\n--------------------- Primer ejercicio: ---------------------")
countLetters(userText, userLetters)
print("\n--------------------- Segundo ejercicio: --------------------")
customeLenght(userText)
print("\n--------------------- Tercero ejercicio: --------------------")
first_and_later(userText)
print("\n--------------------- Cuarto ejercicio: ---------------------")
reverse(userText)
print("\n--------------------- Quinto ejercicio: ---------------------")
fountPython(userText)
