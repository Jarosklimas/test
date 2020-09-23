import calendar as c
import random as r



name = input ('Podaj imię  \n') 
print ('Dwie pierwsze litery', name[:2])
print (name[0]+ name[1])
if name[-1]== 'a':
    print('Imie jest żeński')
else:
        print('Imie jest meskie')

pesel = int(input('Podaj pesel\n'))
print ('Ostatnia cyfra liczby ', pesel, 'to', pesel%10)
if (pesel%10) == 1 :
    print("Jestes osobnikiem męskim")
else:
    print('Jestes osobnikiem żenśkim')
numer = str(pesel)
print ('Rocznik \n', numer[0:2], '\n', 'urodzony \n', numer[2:4], " \n", "w dniu \n", numer[4:6])
y = int (input("Podaj rok :"))
m = int (input("Podaj miesiac :"))
print (c.month(y,m))
                                        #prosi o podanie hasła 
word = input ("Podaj hasło \n ")
if word.lower() =='akademia':
    print("Hasło poprawne")
else:
    print("Hasło niepoprawne")
                                        # dopóki nie podasz poprawnego hasła program bedzie wykonywał petle while. Jesli uzytkownik nie odgadnie hasła bedzie komunikat podaj jeszcze raz hasło
password =input('Podaj hasło jeszcze raz dla uwierzytelnienia użytkownika \n')
secret_password = 'Akademia'
while password!= secret_password:
    password = input ('Niepoprawne hasło podaj jeszcze raz \n')
print('Gratulacje podałes poprawne hasło ')
