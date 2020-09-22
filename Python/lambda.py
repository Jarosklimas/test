suma = lambda a, b : a + b

wynik =suma (3, 5)
print(wynik)
def wypisz_informacje(**kwargs): #kwargs to jest inaczej słownik
    for klucz in kwargs:
        print(f'Pod kluczem {klucz} znajduje sie {kwargs[klucz]}.')

wypisz_informacje (imie='Jarek', nazwisko='Klimczyk')