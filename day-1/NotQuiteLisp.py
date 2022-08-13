# open input.txt and read it
with open('input.txt') as f:
    data = f.read()

# split the data into a list of chars
input = list(data)
floor = 0
counter = 0
reached_below_basement = False
for i in input:
    if floor == -1:
        reached_below_basement = True
    elif not reached_below_basement:
        counter += 1
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
print(floor)
print(counter)