

def condense_csv(filename, id_name='ID'):
    import csv
    file_csv_dict = {id_name:[]}
    with open('data.csv', 'r', encoding='utf-8') as read_file, open('condensed.csv', 'w', encoding='utf-8', newline='') as write_file:
        rfile = csv.reader(read_file)
        for line in rfile:
            if line[0] in file_csv_dict[id_name]:
                file_csv_dict[line[1]] = file_csv_dict.get(line[1], []) + [line[2]]
            else:
                file_csv_dict[id_name] = file_csv_dict.get(id_name, []) + [line[0]]
                file_csv_dict[line[1]] = file_csv_dict.get(line[1], []) + [line[2]]
        collums = [i for i in file_csv_dict.keys()]
        data = []
        for i in range(len(file_csv_dict[id_name])):
            d = []
            for j in range(len(collums)):
               d.append(file_csv_dict[collums[j]][i])
            data.append(d)
        write = csv.writer(write_file)
        write.writerow(collums)
        for row in data:
            write.writerow(row)

text = '''ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none'''

with open('datafiles\data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('datafiles\data.csv', id_name='ID')

# with open('datafiles\condensed.csv', encoding='utf-8') as file:
#     print(file.read().strip())