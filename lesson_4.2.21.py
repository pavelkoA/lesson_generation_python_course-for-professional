

def filter_class(filename):
    import csv
    with open(filename, 'r', encoding='utf-8') as readfiles, open('datafiles/sorted_student_counts.csv', 'w', newline='', encoding='utf-8') as write_file:
        rfiles = csv.DictReader(readfiles)
        n = rfiles.fieldnames
        s = sorted(n[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
        n = ['year']
        for i in s:
            n.append(i)
        write_file = csv.DictWriter(write_file, fieldnames=n, delimiter=',')
        write_file.writeheader()
        for row in rfiles:
            write_file.writerow(row)



filter_class('datafiles/student_counts.csv')