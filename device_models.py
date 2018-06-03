device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}

[{'id': 1, 'name': 'cpu0', 'model': 'Xeon'},
 {'id': 2, 'name': 'mem_bank0', 'model': 'Corsair'}]

{'Xeon': ['cpu0'], 'Corsair': ['mem_bank0', 'mem_bank1']}

devices = []
for dev_id, name in device_names.items():
    model = device_models[dev_id]
    devices.append({'id': dev_id, 'name': name, 'model': model})

print(devices)

model_map = {}

for dev_id, model in device_models.items():
    if model in model_map:
        model_map[model].append(device_names[dev_id])
    else:
        model_map[model] = [device_names[dev_id]]

print(model_map)