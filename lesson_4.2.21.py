

def filter_class(filename):
    import csv
    with open(filename, 'r', encoding='utf-8') as readfiles:
        rfiles = csv.DictReader(readfiles)
        sortdict = sorted(list(rfiles)[0])
        for i in sortdict:
            if i != 'year':
                print(int(i.split('-')[0]))



filter_class('datafiles/student_counts.csv')