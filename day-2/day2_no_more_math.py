with open ('input.txt') as f:
    data = f.read().splitlines()
def calc_area(data):
    l, w, h = map(int, data.split('x'))
    return (l*w, w*h, h*l)

def calc_perimeter(data):
    l, w, h = map(int, data.split('x'))
    return (2*l + 2*w, 2*l + 2*h, 2*w + 2*h)

def calc_paper(data):
    areas = calc_area(data)
    return 2 * sum(areas) + min(areas)

def calc_ribbon(data):
    l, w, h = map(int, data.split('x'))
    perimeters = calc_perimeter(data)
    return min(perimeters) + l * w * h

total_area = sum(map(calc_area, data))
print(total_area)
total_ribbon = sum(map(calc_ribbon, data))
print(total_ribbon)
