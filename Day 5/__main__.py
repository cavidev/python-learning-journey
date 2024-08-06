import os
import time
from random import choice, shuffle

# lifes = "❤️❤️❤️❤️❤️❤️"
heart = "❤️"
error = "❌"
words = {"1": ["guitar",  "butterfly", "computer", "star", "window",
               "elephant", "library", "clock", "journey", "garden", "banana",
               "sky", "truck", "mountain", "piano", "icecream", "tree", "car",
               "vacation", "smile"], "2": ["guitarra", "mariposa", "computadora", "estrella",
                                           "ventana", "elefante", "biblioteca", "reloj", "viaje", "jardín",
                                           "platano", "cielo", "camión", "montaña", "piano", "helado", "árbol",
                                           "coche", "vacaciones", "sonrisa"]}


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def replace_at(string, id, char):
    return string[:id] + char + string[id+1:]


def masthead(heart, lifes):
    print("#"*20)
    print(f"{'#'*7} GAME {'#'*7}")
    print("#"*20)
    print(f"{heart}{' ' * len(heart)}{lifes}\n")


def print_error():
    clean()
    print(f"{'#'*20}\n{' '*20}\n{' '*20}")
    print(f"{' '*9}{error}{' '*9}")
    print(f"{' '*20}\n{' '*20}\n{'#'*20}")
    time.sleep(1)


def print_win():
    clean()
    print(f"{'#'*20}\n{' '*20}\n{' '*20}")
    print(f"{' '*9}{'🏆'}{' '*9}")
    print(f"{' '*20}\n{' '*20}\n{'#'*20}")
    play_again = input("restart? yes/no : ").upper()
    if (play_again == "YES"):
        main()


def logic(char, word, lifes, secrectWord):
    if char in word and not char in secrectWord:
        slave = 0
        for i in range(len(word)):
            slave += 1
            if word[i] == char:
                secrectWord = replace_at(secrectWord, i+slave, char)
        if secrectWord.replace(" ", "") == word:
            print_win()
            return True
    else:
        lifes = lifes-1
        print_error()
        return False


def game(word):
    clean()
    lifes = 6
    secrectWord = " " + "_ "*len(word)
    while True:
        clean()
        masthead(heart, lifes)
        print(f"{secrectWord}\n")
        char = input(":: ")
        if char in word and not char in secrectWord:
            slave = 0
            for i in range(len(word)):
                slave += 1
                if word[i] == char:
                    secrectWord = replace_at(secrectWord, i+slave, char)
            if secrectWord.replace(" ", "") == word:
                print_win()
                return True
        else:
            lifes = lifes-1
            print_error()
            return False
        if lifes == 0:
            print(word)
            break


def main():
    print("-" * 20)
    text = "Hi/Hola"
    print(f"| {text:^17} |")
    print("-" * 20)
    lenguaje = input("1: English\n2: Español\n:: ")
    shuffle(words.get(lenguaje))
    word = choice(words.get(lenguaje))
    game(word)


if __name__ == "__main__":
    main()
