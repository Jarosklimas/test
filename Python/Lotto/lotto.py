import random as r 
import calendar as c
import pylab



print('*'*10, "Podaj date kolejnego losowania ", '*'*10)
y = int (input("Podaj rok :"))
m = int (input("Podaj miesiac :"))
d = int(input("Podaj dzień : "))
print('*'*10, "Podaj liczby jakie zostały wylosowane", '*'*10)
kula_1 = int (input("Podaj pierwsza liczbe ;" ))
kula_2 = int (input("Podaj druga liczbe ;" ))
kula_3 = int (input("Podaj trzecia liczbe ;" ))
kula_4 = int (input("Podaj czwarta liczbe ;" ))
kula_5 = int (input("Podaj piata liczbe ;" ))
kula_6 = int (input("Podaj szosta liczbe ;" ))

x = range (1, 6)
w= [] #lista wartosci
for i in x:
    w.append(kula_1*i*i*i*i+kula_2*i*i*i+ kula_3*i*i + kula_4*i*i+kula_5*i+kula_6)

pylab.plot(x,w)
pylab.title('Wykres F(x) = a*i + b ')
pylab.grid(True)
#pylab.show()


print (c.month(y,m))
print('*'*10,"Tego dnia padna takie oto liczby",'*'*10)
for i in range(1,50):
    if i < 7:
        lotto= r.randrange(1, 50)
        print( lotto)
print('*'*10,"Biegni spełniać marzenia",'*'*10)