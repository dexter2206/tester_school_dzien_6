data = [{'id': 1, 'model': 'AFE2'}, {'id': 2, 'model': 'FB12'}]

for record in data:
    print(record['id'])

print([record['id'] for record in data])