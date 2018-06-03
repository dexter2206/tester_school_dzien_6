dev_ids = []

for i in range(1, 5):
    dev_ids.append('device_' + str(i))

print(dev_ids)
print(['device_' + str(i) for i in range(1, 5)])