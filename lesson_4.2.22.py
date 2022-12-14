import csv

with open('prices.csv', 'r', encoding='utf-8') as read_files:
    rfiles = csv.DictReader(read_files, delimiter=';')
    prod_dict = {}
    for line in rfiles:
        prod_dict[line['Магазин']] = min(list(line.items())[1:], key=lambda x: int(x[1]))
    result = sorted(prod_dict.items(), key=lambda x: (int(x[1][1]), x[1][0]))[0]
    print(f'{result[1][0]}: {result[0]}')