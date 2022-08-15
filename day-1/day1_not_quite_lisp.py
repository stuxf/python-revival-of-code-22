with open('input.txt') as f:
    data = f.read().strip()

instructions = { "(": 1, ")": -1 }

floor = 0
basement_counter = None

for count, instruction in enumerate(data):
    if floor == -1 and basement_counter is None:
        basement_counter = count
    floor += instructions[instruction]

print(f"Santa ends up on floor {floor}")
print(f"Santa enters the basement on instruction {basement_counter}")