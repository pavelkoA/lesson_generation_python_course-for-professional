
def unite_files(file1, file2):
    import json
    with open(file1, 'r', encoding='utf-8') as file1, open(file2, 'r', encoding='utf-8') as file2, open('datafiles/data_merge.json', 'w', encoding='utf-8') as write:
        unite_dict = {}
        rfile1 = json.load(file1)
        rfile2 = json.load(file2)
        for key, value in rfile1.items():
            unite_dict[key] = value
        for key, value in rfile2.items():
            unite_dict[key] = value
        json.dump(unite_dict, write, indent=2)


unite_files('datafiles/data1.json', 'datafiles/data2.json')