import csv

# Open the CSV file
with open('wyniki-lotto.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    #for row in reader:
    #  print (row)
    # Seek to the end of the file
    file.seek(0, 2)
    # Go back one row
    file.seek(file.tell() - 16)

    # Read the last row
  
    last_row = next(reader)
    print(last_row)