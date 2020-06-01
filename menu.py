import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("|--------------------------------------------------------------|")
print("|   Witamy w projekcie biometrycznym na temat keystrokingu     |")
print("|                                                              |")
print("| All rights reserved for Krzystof Miodonski and Adam Bachera  |")
print("|--------------------------------------------------------------|\n")
print("Twoje opcje:")
print("1. Stworz nowy profil. (Pamietaj, jest to dlugi proces.)")

wybor = int(input("\nPowiedz nam co chcesz zrobic: "))

if wybor == 1:
    name = input("\n Podaj nazwe profilu: ")
    while True:
        try:
            os.makedirs(name)
            os.chdir(name)
            break
        except FileExistsError:
            print ("Istnieje profil o tej nazwie, wybierz inna: ")
            name = input("\n Podaj nazwe profilu: ")

    clear_screen()
    exec(open("../tworzeniemodelu.py").read())