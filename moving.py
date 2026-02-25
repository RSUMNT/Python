import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

random_name = 'i\'m '

print(random_name) 
try:
    with open('packing_list.csv', 'r', newline='', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File not found. Creating a new packing list.")
    with open('packing_list.csv', 'w', newline='', encoding='utf8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

