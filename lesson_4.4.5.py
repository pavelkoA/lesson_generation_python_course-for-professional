import json

def is_correct_json(file):
    try:
        j = json.loads(file)
    except:
        return False
    return True

data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))

print(is_correct_json('number = 17'))
