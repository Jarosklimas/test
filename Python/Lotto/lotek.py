#!/usr/bin/env python
# -*- coding: utf -8 -*-
 
from lxml import html
from datetime import date
import requests
import xlwt
from bs4 import BeautifulSoup
from requests import get
import xlrd

URL ="http://www.mbnet.com.pl/dl.xls"
URL2 = "http://www.mbnet.com.pl/dl.txt"
URL3 ="http://www.mbnet.com.pl/bazalosl.zip"
response = requests.get(URL)

r = requests.get(URL2)
b = requests.get(URL3)

filepath = 'D:/priv_repo/test/Python/dl.xls'
filepath2 = 'D:/priv_repo/test/Python/dl.txt'
filepath3 ="D:/priv_repo/test/Python/bazalosl.zip"


with open(filepath, 'wb') as f:
    f.write(response.content)
    f.close
#otwarcie pliku
#file_1 = xlwt.Workbook(encoding="utf-8")
with open(filepath2, 'wb') as f2:
    f2.write(r.content)
    f2.close
with open(filepath3, 'wb') as f3:
    f3.write(b.content)
    f3.close

file_1 = xlrd.open_workbook("D:/priv_repo/test/Python/dl.xls")
for sheet_name in file_1.sheet_names():
    arkusz = file_1.sheet_by_name(sheet_name)
    print (arkusz.row_values(-1)[4],)
    print (arkusz.row_values(-1)[4],)
    print (arkusz.row_values(-1)[4],)
    f.close



#f.read(8)
#URL = 'http://www.mbnet.com.pl/wyniki.htm'

#page = get (URL)
#bs = BeautifulSoup(page.content)

#for offer in bs.find_all('a'):
#    print(offer)
#print(page.content)


'''
# kodowanie arkusza 
baza = xlwt.Workbook(encoding="utf-8")




#tworze konkretną ilość arkuszy
sheet1 = baza.add_sheet("Wyniki")
sheet2 = baza.add_sheet("Dane")
#pobieram dzisiejszą datę
today = date.today()
# format wyświetlanej daty
data = today.strftime('%d-%m-%Y')
#adres strony z horoskopem
urlwyborcza = "http://www.mbnet.com.pl/dl.xls"
urlwyborcza += data

#ścieżka do elementu XPATH
xpathwyborcza = '//*[@a="holder_230"]/div/a[1]/text()'
#pobiera stronę z horoskopem
pagewyborcza = requests.get(urlwyborcza)
#parsuje stronę
tree= html.fromstring(pagewyborcza.text)
# wyszukuje interesujący nas element
textwyborcza = tree.xpath(xpathwyborcza)
# wyświetla w yniki działania

print(data)
print (pagewyborcza)
print (tree)
print (textwyborcza)
'''
