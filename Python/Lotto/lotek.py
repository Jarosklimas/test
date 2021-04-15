#!/usr/bin/env python
# -*- coding: utf -8 -*-

from lxml import html
from datetime import date
import requests
import xlwt
from bs4 import BeautifulSoup
from requests import get
import xlrd
import pandas as pd
import numpy as np
import random

#----------------------------------------------------------------------To jest sekcja do pobierania  danych oraz zczytywania ----------------------------------------------------------------------
URL = "http://www.mbnet.com.pl/dl.xls"
URL2 = "http://www.mbnet.com.pl/dl.txt"
URL3 = "http://www.mbnet.com.pl/bazalosl.zip"
response = requests.get(URL)

r = requests.get(URL2)
b = requests.get(URL3)

filepath = 'D:/priv_repo/test/Python/dl.xls'
filepath2 = 'D:/priv_repo/test/Python/dl.txt'
filepath3 = "D:/priv_repo/test/Python/bazalosl.zip"

'''
with open(filepath, 'wb') as f:
    f.write(response.content)
    f.close
# otwarcie pliku
# file_1 = xlwt.Workbook(encoding="utf-8")
with open(filepath2, 'wb') as f2:
    f2.write(r.content)
    f2.close
with open(filepath3, 'wb') as f3:
    f3.write(b.content)
    f3.close 
'''
#--------------------------------------------------------------------------------koniec---------------------------------------------------------------------------------------
#----------------------------------------------------------------------To jest sekcja do losowania liczb----------------------------------------------------------------------
liczby = []
ileliczb = 6
maksliczba = 49
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1
print("Wylosowane liczby to :", liczby)


def losowanie_liczb():
    liczby = []
    ileliczb = 6
    maksliczba = 49
    i = 0

    while i < ileliczb:
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1

    print("Wylosowane liczby to :", liczby)
#--------------------------------------------------------------------------------------koniec-----------------------------------------------------------------------------------------

def data_from_excel(filepath):
    data_list = []
    data = xlrd.open_workbook(filepath)
    sheet = data.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        data_list.append(sheet.cell_value(i, 0))
    return print(data_list)


# "D:/priv_repo/test/Python/dl.xls"
#"C:/repozytorium/test/Python/dl.xls"
file_1 = xlrd.open_workbook("D:/priv_repo/test/Python/dl.xls")
print("The number of worksheets is", file_1.nsheets)
print("Worksheet name(s):", file_1.sheet_names())
sh = file_1.sheet_by_index(0)
#--------------------------------------------------------------------------------------wyświetlenie kolumn w postaci wierszy ------------------------------------------------------------
for rowx in range(-6, 0):
    licz_cyfre = 1
    if licz_cyfre <=49:
        cyfra = sh.col_values(rowx)[-20:]
        licz=cyfra.count(licz_cyfre)
        print("Kolumna  to :",rowx, cyfra)
        print("1\n",licz)
        licz_cyfre = licz_cyfre +1
#--------------------------------------------------------------------------------------koniec-----------------------------------------------------------------------------------------
print(sh.name, sh.nrows, sh.ncols)
print("Cell D30 is", sh.cell_value(rowx=29, colx=3))


ilosc_column = -6
licz_cyfre = 1
liczniki_19 = []
y = 0 
cunter = []
while ilosc_column <= -1:
    lista = sh.col_values(ilosc_column)[-20:]  # ostatnia kolumna w arkuszuS
    print ("jest to kolumna :", ilosc_column)
    licz_cyfre = 1
    
    while licz_cyfre <= 49  :
        wynik = lista.count(licz_cyfre)
        print("Liczb nr ", licz_cyfre, " w kolumnie ",ilosc_column,"jest", wynik )
        #liczniki_19.append(wynik)
        #print ("to jest pierwszy  licznik_19 ",liczniki_19)
        
        licz_wynik = list(range(wynik))
        cunter.append(wynik)
        print ("To jest licznik wyniku",licz_cyfre, licz_wynik, "\n")
        licz_cyfre = licz_cyfre +1
    ilosc_column = ilosc_column +1
    print (cunter) 
    
    
    for licz_cyfre in range (wynik):
        liczniki_19.append(wynik)
        #print ("to jest licznik_19 ",liczniki_19)
    for licz_cyfre in range(wynik):
            y = y + liczniki_19[licz_wynik]
print("Suma wartosci elementów  listy to {0}".format(y))

print ("                                 **************\tIlosc kolumn równa sie :\t", ilosc_column," Licznik przestaje liczyć ilość wystąpienia poszczególnych liczb **************")
print("Ilość 19 to :", liczniki_19)
print("Wierszy jest :", len(lista))

for sheet_name in file_1.sheet_names():
    arkusz = file_1.sheet_by_name(sheet_name)
# ------------------------------------------------ robi macierz z konketynch 20 wierszy ----------------------------------------------------------------------------------------------------------
'''
rx = -20
i = 0
while i < 20:
    wiersz = arkusz.row_values(rx)[2:]
    #print("to jest wiersz  ", rx, "które mają wartość", wiersz)
    losowanie = np.array(wiersz)
    print(losowanie)
    if (rx < 1):
        rx = rx + 1
        i = i+1
for element in losowanie.flat:
            #jedynka= element.count(1)
            print()
'''

# ---------------------------------------------------- koniec---------------------------------------------------------------------------------------------------------------------------------------
wiersz_ost = arkusz.row_values(-1)[2:]
wiersz_przed_osta = arkusz.row_values(-2)[2:]
wiersz_20_od_konca = arkusz.row_values(-20)[2:]

porównanie = list(set(wiersz_ost).intersection(set(wiersz_przed_osta)))

print("\n\n\nOstatnie losowanie \t\t\t\t : ", wiersz_ost)
print("Przedostatnie losowanie to\t\t\t : ", wiersz_przed_osta)
print("Ta sama liczba w dwóch ostatnich losowaniach to  : ", porównanie)


# ------------------------------------------------ robi macierz od 0-48----------------------------------------------------------------------------------------------------------
'''
macierz = np.arange(49).reshape(7, 7)
print(macierz)
'''
#-------------------------------------------------------koniec-------------------------------------------------------------------------------------------------------------------



#print(arkusz.name)

# f.read(8)
# URL = 'http://www.mbnet.com.pl/wyniki.htm'

# page = get (URL)
# bs = BeautifulSoup(page.content)

# for offer in bs.find_all('a'):
#    print(offer)
# print(page.content)


'''
# kodowanie arkusza
baza = xlwt.Workbook(encoding="utf-8")




# tworze konkretną ilość arkuszy
sheet1 = baza.add_sheet("Wyniki")
sheet2 = baza.add_sheet("Dane")
# pobieram dzisiejszą datę
today = date.today()
# format wyświetlanej daty
data = today.strftime('%d-%m-%Y')
# adres strony z horoskopem
urlwyborcza = "http://www.mbnet.com.pl/dl.xls"
urlwyborcza += data

# ścieżka do elementu XPATH
xpathwyborcza = '//*[@a="holder_230"]/div/a[1]/text()'
# pobiera stronę z horoskopem
pagewyborcza = requests.get(urlwyborcza)
# parsuje stronę
tree= html.fromstring(pagewyborcza.text)
# wyszukuje interesujący nas element
textwyborcza = tree.xpath(xpathwyborcza)
# wyświetla w yniki działania

print(data)
print (pagewyborcza)
print (tree)
print (textwyborcza)
'''
