import json

numbers = [2, 3, 5, 7, 9, 11, 15]
filename = "py1000/numbers.json"

with open(filename, "w") as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers2 = json.load(f)

print(numbers2)