

def filter_class(filename):
    import csv
    with open(filename, 'r', encoding='utf-8') as readfiles:
        rfiles = csv.DictReader(readfiles)
        for line in rfiles:
            for i in line.items():
                print(i[0].split('-'))



filter_class('datafiles/student_counts.csv')