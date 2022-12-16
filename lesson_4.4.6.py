import json
import sys

in_stringe = json.load(sys.stdin)

for key, value in in_stringe.items():
    if type(value) == list:
        print(f'{key}:', end=' ')
        print(*value, sep=', ')
    else:
        print(f'{key}: {value}')
