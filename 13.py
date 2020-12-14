array = []
with open("input.txt","r") as f:
	n = int(f.readline().strip())
	array = [x for x in f.readline().split(',')]

input1 = [int(x) for x in array if x != 'x']

maximum = float('inf') 
bus = 0

for i in input1:
	time = i - n % i
	if time <= maximum:
		bus = i
		maximum = time

print(bus * maximum)	

t = 0
step = 1
for i in range(len(array)):
	if array[i] != 'x':
		bus = int(array[i])
		while (t + i) % bus != 0:
			t += step
		step *= bus

print(t)
