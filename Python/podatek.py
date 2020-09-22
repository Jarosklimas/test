from math import sqrt

def policz_brutto(netto, stawka_vat):
        return netto +netto * stawka_vat

cena = 1000
stawka_vat = 0.23
brutto = policz_brutto(cena, stawka_vat)
print(f'Produkt o cenie {cena} i stawka vat {stawka_vat} kosztuje {brutto} PLN')
print(f'Produkt o cenie 200 i stawka vat 0.23 kosztuje {policz_brutto(200, 0.23)} PLN')


def policz_dlugosc_odcinka(x1, x2, y1, y2):
    return sqrt ((x1-x2)**2 + (y1-y2)**2)

print("Długość odcinka wynosi ", policz_dlugosc_odcinka(x1=2, y1=2, x2=5, y2=5))

def policz_wyplate(podstawa, premia_rzad=0, premia_klienta=0, hajs_z_youtube=0):
    return podstawa + premia_klienta + premia_rzad + hajs_z_youtube

pensja= policz_wyplate (1000,1500)
print (f'Zarobiłem {pensja}')
print (f'Zarobiłem, podejście drugie {policz_wyplate(1000, hajs_z_youtube=1000)}')

def policz_srednia(*args):
    return sum (args) / len(args)
print (policz_srednia (2,3,5))
print(policz_srednia (5, 6, 4, 2))

def wypisz_informacje(**kwargs): #kwargs to jest inaczej słownik
    for klucz in kwargs:
        print(f'Pod kluczem {klucz} znajduje sie {kwargs[klucz]}.')

wypisz_informacje (imie='Jarek', nazwisko='Klimczyk')