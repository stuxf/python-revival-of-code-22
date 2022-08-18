with open('input.txt') as f:
    data = f.read()

x = 0
y = 0
robo_x = 0
robo_y = 0
houses = {(x, y)}
for count, direction in enumerate(data):
    if count % 2 == 0:
        match direction:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        houses.add((x, y))
    else:
        match direction:
            case '>':
                robo_x += 1
            case '<':
                robo_x -= 1
            case '^':
                robo_y += 1
            case 'v':
                robo_y -= 1
        houses.add((robo_x, robo_y))
print(len(houses))