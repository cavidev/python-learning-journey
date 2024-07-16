from random import randint
from colorama import init, Fore, Style


message = "he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número"

numberAI = randint(1, 101)
namePlayer = input("Escribe tu nombre: ")
print(f"Bueno, {namePlayer}, {message}")


# Inicializar colorama
init()


def logError(message, color=Fore.RED):
    print(f"Error: {color} {message} {Style.RESET_ALL}")


def logWarning(message, color=Fore.YELLOW):
    print(f"Warning: {color} {message} {Style.RESET_ALL}")


def main():
    tries = 8
    while (tries > 0):
        try:
            numberUser = int(input("Dime tu número: "))
        except ValueError:
            logError("Por favor, ingresa un número válido.")
            continue
        if (numberUser < 1 or numberUser > 100):
            logError("Este numero se sale del rango de 1 a 100")
        elif (numberUser < numberAI):
            logWarning(
                "su respuesta es incorrecta y has elegido un número menor al número secreto")
        elif (numberUser > numberAI):
            logWarning(
                "su respuesta es incorrecta y has elegido un número mayor al número secreto")
        elif (numberUser == numberAI):
            print(f"Ganaste 🏆 con {8 - tries} intentos")
            break

        tries -= 1

        if tries == 0:
            print(
                f"Lo siento ❌, no has adivinado el número. El número secreto era {numberAI}.")
        else:
            print(f"Te quedan {tries} intentos.")


if __name__ == "__main__":
    main()
