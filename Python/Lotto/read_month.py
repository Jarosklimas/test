
import csv

with open('d:/priv_repo/test/Python/Lotto/totolotto/wyniki-lotto.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Przewijanie do ostatniego wiersza
    for row in csv_reader:
        last_row = row
    ost_wiersz = last_row[-1]
    balls = ost_wiersz.split(';')
    print((balls[4]))