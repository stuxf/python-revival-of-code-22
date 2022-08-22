with open ('input.txt') as f:
    data = f.read().splitlines()

# initialize 1000x1000 2d array of 0 values
lights = [[False for i in range(1000)] for j in range(1000)]

def turn_on(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights[i][j] = True

def turn_off(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights[i][j] = False

def toggle(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights[i][j] = not lights[i][j]

for instruction in data:
    x1, y1 = tuple(map(int, instruction.split()[-3].split(',')))
    x2, y2 = tuple(map(int, instruction.split()[-1].split(',')))
    if instruction.startswith('turn on'):
        turn_on(x1, y1, x2, y2)
    elif instruction.startswith('turn off'):
        turn_off(x1, y1, x2, y2)
    elif instruction.startswith('toggle'):
        toggle(int(x1), int(y1), int(x2), int(y2))

print(sum(sum(lights, [])))

# Part 2
lights_2 = [[0 for i in range(1000)] for j in range(1000)]

def turn_on_2(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights_2[i][j] += 1

def turn_off_2(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights_2[i][j] = max(0, lights_2[i][j] - 1)

def toggle_2(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights_2[i][j] += 2

for instruction in data:
    x1, y1 = tuple(map(int, instruction.split()[-3].split(',')))
    x2, y2 = tuple(map(int, instruction.split()[-1].split(',')))
    if instruction.startswith('turn on'):
        turn_on_2(x1, y1, x2, y2)
    elif instruction.startswith('turn off'):
        turn_off_2(x1, y1, x2, y2)
    elif instruction.startswith('toggle'):
        toggle_2(x1, y1, x2, y2)

print(sum(sum(lights_2, [])))