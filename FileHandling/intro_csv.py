import csv

# with open('data.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# CSV values are read as strings by the csv module.
# DictReader() ⭐⭐⭐
# Useful when the CSV has column names

# with open('data.csv', 'r', newline='') as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row['city'])

# Writing csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Abhilash', '24', 'Cuttack'])
    writer.writerow(['Bruce', '45', 'Gotham'])
    writer.writerow(['Tony', '55', 'New york'])
    writer.writerow(['Tony', '55', 'New york'])


