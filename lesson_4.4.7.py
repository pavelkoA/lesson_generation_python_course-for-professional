import json

with open('datafiles/data.json', 'r', encoding='utf-8') as file, open('datafiles/updated_data.json', 'w', encoding='utf-8') as write:
    rfile = json.load(file)
    result_string = []
    for line in rfile:
        if type(line) == str:
            result_string.append(line + '!')
        elif type(line) == int or type(line) == float:
            result_string.append(line + 1)
        elif type(line) == bool:
            if line == True:
                result_string.append(False)
            else:
                result_string.append(True)
        elif type(line) == list:
            result_string.append(line * 2)
        elif type(line) == dict:
            line['newkey'] = None
            result_string.append(line)
        elif line == None:
            continue
    json.dump(result_string, write, indent=2)