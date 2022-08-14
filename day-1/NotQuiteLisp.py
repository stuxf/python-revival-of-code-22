with open('input.txt') as f:
    data = f.read()

floor = 0
basement_counter = None

for count, instruction in enumerate(data):
    if floor == -1 and basement_counter is None:
        basement_counter = count
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1

print(f"Santa ends up on floor {floor}")
print(f"Santa enters the basement on instruction {basement_counter}")