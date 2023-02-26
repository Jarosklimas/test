
numbers = [[1,2,2], [4, 5, 6], [1, 2, 3]]
result_data = {}
count = 0
search_number = 1
ile_losowan = int(input("podaj ile wyswietlic list"))
sublist = numbers [-ile_losowan :]
print(sublist)

def count_number (search_number):
    
    count = 0
    
    for number in sublist:
        count += number.count(search_number)
   
    return count # Output: 3

while search_number <= 49:
    #print("Dana liczba ", search_number,'\n')
    #print(count_number(search_number),'\n')
    
    #print(search_number,'\n')
    result_data[search_number] = (count_number(search_number))
    
    print(search_number, 'występuje', result_data[search_number], 'razy')

    search_number = search_number +1  
    dic = result_data.items()
print (dic)