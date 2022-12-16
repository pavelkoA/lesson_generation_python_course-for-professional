import json

def is_correct_json(file):
    try:
        return True if json.loads(file) else False
    except:
        return False

data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))

print(is_correct_json('number = 17'))
