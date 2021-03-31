from requests import get
from json import loads # load to pozwala odczytac z pliku u nas na dysku, 
                       # loads- zamianic na liste słowników coś co jest stringiem 
from terminaltables import AsciiTable

CITIS = ['Gdańsk','Warszawa', 'Łódź']
def main ():
    url ='https://danepubliczne.imgw.pl/api/data/synop'
    response= (get(url))
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Cisnienie'] # to są etykiety moich kolumn mozna uzyć dowolnych nazw (tworzymy listę list)
    ]

    for row in loads(response.text):
        if row ['stacja'] in CITIS:
            rows.append([                            # jeżeli chce wyswietlać dane tylko niektóe z tych kolumn to potrzebujem je dodawać do listy rows
                row['stacja'],                       # tu znajduje sie Masto 
                row['godzina_pomiaru'],              # tu znajduje sie godzina pomiaru 
                row['temperatura'],                  # tu znajduje sie temperatura
                row['cisnienie']
            ])

    table =AsciiTable(rows) # wyswietlanie danych w formie tabelki wiec trzeba stworzyć obiekt 
    print(table.table)
            #print(row)
   # print (loads(response.text))

if __name__ == '__main__':
    print('Pogodynka 2020')
    main()