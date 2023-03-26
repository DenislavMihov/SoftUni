data = input()
list_of_resources = []
collected_resources = {}

while data != "stop":
    list_of_resources.append(data)
    data = input()

for index in range(0, len(list_of_resources), 2):
    key = list_of_resources[index]
    value = int(list_of_resources[index+1])
    if key in collected_resources:
        collected_resources[key] += value
    else:
        collected_resources[key] = value

for resource, quantity in collected_resources.items():
    print(f"{resource} -> {quantity}")