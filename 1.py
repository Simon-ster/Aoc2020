array = []
with open("input1.txt",'r') as input:
	for line in input.readlines():
		array.append(int(line.strip()))

for i in range(len(array)):
	for j in range(i+1,len(array)):
		for k in range(j+1,len(array)):
			if array[i]+array[j] == 2020:
				p1 = "part 1: "+ str(array[i]*array[j])
				break
			elif array[i]+array[j]+array[k] == 2020:
				p2 = "part 2: "+ str(array[i]*array[j]*array[k])

print(p1)
print(p2)