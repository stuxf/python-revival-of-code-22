import hashlib
with open ('input.txt') as f:
    data = f.read().strip()
counter = 0
while True:
    hash = hashlib.md5((data + str(counter)).encode('utf-8')).hexdigest()
    if hash[:6] == '000000':
        print(counter)
        break
    counter += 1