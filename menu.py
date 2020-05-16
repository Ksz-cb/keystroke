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
    clear_screen()
    exec(open("./test.py").read())

