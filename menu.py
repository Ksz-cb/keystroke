import test.py

print("Witamy w projekcie biometrycznym na temat keystrokingu")
print("All rights reserved for Krzystof Miodonski and Adam Bachera")
print("-----------------------------------------------------------")
print("Twoje opcje:")
print("1. Stworz nowy profil. (Pamietaj, jest to dlugi proces.)")

wybor=input("\nPowiedz nam co chcesz zrobic:")

if wybor == 1:
    execfile('python test.py')