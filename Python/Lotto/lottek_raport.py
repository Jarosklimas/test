import openpyxl
import os

class Lotto ():
    
    def __init__ (self):
        self.workbook = openpyxl.Workbook()
        
    def write_the_geomet_average(self):
        
      
        worksheet = self.workbook.active       
        worksheet.column_dimensions['A'].width = 20
        worksheet.cell(row=1, column=1).value = "Geomet_average"
     
        
        self.workbook.save(os.path.dirname(__file__) +"/Lotto_1.xlsx")
        
emp1 = Lotto()
emp1.write_the_geomet_average()