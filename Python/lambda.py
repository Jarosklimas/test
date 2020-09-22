suma = lambda a, b : a + b

wynik =suma (3, 5)
print(wynik)
def policz_wyplate(podstawa, policz_premie):
    return podstawa +policz_premie(podstawa)

def zwroc_zero (podstawa):
    return 0
def policz_premie_managera(podstawa):
    return 0.5 * podstawa
print(policz_wyplate (1000, zwroc_zero))
print(policz_wyplate(2000, policz_premie_managera))
print(policz_wyplate(3000, lambda x: x*0.25))