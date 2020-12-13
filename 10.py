array = [0]
with open("input10.txt",'r') as input:
	for line in input.readlines():
		x = line.strip()
		array.append(int(x))
 
array.sort()
array.append(array[len(array)-1]+3)

one = 0
three = 0
n = len(array) - 1

dynamic = n * [0]
dynamic[0] = 1

for i in range(n):
    if array[i+1] - array[i] == 1:
        one += 1
    elif array[i+1] - array[i] == 3:
        three += 1

for i in range(n):
    for j in range(i):
        if array[i] - array[j] <= 3:
            dynamic[i] += dynamic[j]

print("part 1: "+ str(one * three))
print("part 2: "+ str(dynamic[n-1]))