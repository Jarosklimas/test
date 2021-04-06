import random as r
import calendar as c
import pylab

a = 1
b = 2
x = range(-10, 11)
w = []  # lista wartosci
for i in x:
    w.append(a*i+b)

#pylab.plot(x, w)
#pylab.title('Wykres F(x) = a*i + b ')
#pylab.grid(True)
#pylab.show()

print('*'*10, "Podaj date kolejnego losowania ", '*'*10)
y = int(input("Podaj rok :"))
m = int(input("Podaj miesiac :"))
d = int(input("Podaj dzień : "))
print(c.month(y, m))
print('*'*10, "Tego dnia padna takie oto liczby", '*'*10)
for i in range(1, 50):
    if i < 7:
        lotto = r.randrange(1, 50)
        print(lotto)
print('*'*10, "Biegni spełniać marzenia", '*'*10)
