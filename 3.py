array = []
with open("input3.txt",'r') as input:
	for line in input.readlines():
	    array.append(line.strip())

wid = len(array[0]) - 1
x = 0
y = 0
count = 0



while y < len(array):
    if array[y][x] == '#':
        count += 1
    
    x += 1
    y += 2

    if x > wid:
        x -= wid + 1

print(count)