lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Define a function that takes an element as input and returns its square
def geomet_average(lista):   
    
    iloczyn=1
    for liczba in lista:
        # mnozenie kolejnych liczby
        iloczyn *=liczba
    #dlugość listy
    n=len(lista)
    print(n)
    return iloczyn**(1/n)

# Apply the function to each element in the lists
result = [list(map(geomet_average, lst)) for lst in lists]

# Print the result
print(result)