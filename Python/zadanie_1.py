import calendar as c

name = input ('Podaj imię  \n') 

print ('dwie pierwsze litery', name[:2])
print (name[0]+ name[1])

if name[-1]== 'a':
    print('Imie jest żeński')
else:
        print('Imie jest meskie')

pesel = input('Podaj pesel\n')
#print ('Ostatnia cyfra liczy ', pesel, 'to' , pesel%10)
print ('Rocznik ', pesel[0:2], 'urodzony', pesel[2:4], "w dniu", pesel[4:6])

print(c.month (2016,2))