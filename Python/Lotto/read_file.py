import xlrd
import random as r 
import xlwt

'''
# kodowanie arkusza
book = xlwt.Workbook(encoding="utf-8")

# tworzymy dowolną ilość arkuszy (zakładek)
sheet1 = book.add_sheet("Raport ostatnich 10 losowań ")
sheet2 = book.add_sheet("Zestawienie ostatnich losowań ")

# zapisujemy do pliku
book.save("D:\priv_repo\test\Python\Lotto\raport.xls")
'''

#def readLastline():
file_1 = xlrd.open_workbook("D:/priv_repo/test/Python/dl.xls")
for sheet_name in file_1.sheet_names():
    arkusz = file_1.sheet_by_name(sheet_name)
    last_row =(
        arkusz.row_values(-1)[0], 
        arkusz.row_values(-1)[1], 
        arkusz.row_values(-1)[2], 
        arkusz.row_values(-1)[3], 
        arkusz.row_values(-1)[4], 
        arkusz.row_values(-1)[5], 
        arkusz.row_values(-1)[6], 
        arkusz.row_values(-1)[7] 
        
        )
    secound_last_row =(
        arkusz.row_values(-2)[0], 
        arkusz.row_values(-2)[1], 
        arkusz.row_values(-2)[2], 
        arkusz.row_values(-2)[3], 
        arkusz.row_values(-2)[4], 
        arkusz.row_values(-2)[5], 
        arkusz.row_values(-2)[6], 
        arkusz.row_values(-2)[7] 
        
        )
    third_last_row =(
        arkusz.row_values(-3)[0], 
        arkusz.row_values(-3)[1], 
        arkusz.row_values(-3)[2], 
        arkusz.row_values(-3)[3], 
        arkusz.row_values(-3)[4], 
        arkusz.row_values(-3)[5], 
        arkusz.row_values(-3)[6], 
        arkusz.row_values(-3)[7] 
        
        )
    fourth_last_row =(
        arkusz.row_values(-4)[0], 
        arkusz.row_values(-4)[1], 
        arkusz.row_values(-4)[2], 
        arkusz.row_values(-4)[3], 
        arkusz.row_values(-4)[4], 
        arkusz.row_values(-4)[5], 
        arkusz.row_values(-4)[6], 
        arkusz.row_values(-4)[7] 
        
        )
    print(last_row)
    print(secound_last_row)
    print(third_last_row)
    print(fourth_last_row)

    for i in range(1,50):
        if i < 7:
            lotto= r.randrange(1, 50)

            print( lotto)
    print('*'*10,"Biegni spełniać marzenia",'*'*10)