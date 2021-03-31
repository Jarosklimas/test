import xlwt
import xlrd

# kodowanie arkusza
book = xlwt.Workbook(encoding="utf-8")

# tworzymy dowolną ilość arkuszy (zakładek)
sheet1 = book.add_sheet("Raport zbiorczy")
sheet2 = book.add_sheet("Zestawienie wydatków")
sheet3 = book.add_sheet("Zestawienie przychodów")
'''
# umieszczamy w nich dane
sheet1.write(0, 0, "Tutaj jakiś bardzo ważny raport")
sheet2.write(1, 10, "Wydaliśmy dużo")
sheet3.write(0, 2, "Ale zapłacili nam więcej")
sheet3.write(1, 2, "I jeszcze więcej nam zapłacą")
sheet3.write(2, 2, "Będzie fajowo")
'''
# zapisujemy do pliku
book.save("raport.xls")


# otwarcie pliku
book = xlrd.open_workbook("D:\priv_repo\test\Python\Lotto\raport.xls")

# dla każdego arkusza wyświetlamy zawartość pola 0,0
for sheet_name in book.sheet_names():
	arkusz = book.sheet_by_name(sheet_name)
	print(arkusz.row_values(0)[0])

