import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Witamy w projekcie biometrycznym na temat keystrokingu")
print("All rights reserved for Krzystof Miodonski and Adam Bachera")
print("-----------------------------------------------------------")
print("Twoje opcje:")
print("1. Stworz nowy profil. (Pamietaj, jest to dlugi proces.)")

wybor = int(input("\nPowiedz nam co chcesz zrobic: "))

if wybor == 1:
    exec(open("./test.py").read())

