import csv

with open('Bestseller.csv', 'r', newline = '' ,  encoding='utf8') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    max_sales =0 
    best_book = []

    for row in csv_reader:
        sales =float(row[4])
        if sales > max_sales:
            max_sales = sales
            best_book = row

with open('bestseller_info.csv', 'w', newline = '', encoding='utf8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerow(best_book)