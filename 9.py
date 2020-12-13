const = 25
array = []
with open("input9.txt") as input:
	for line in input.readlines():
		array.append(int(line.strip()))

preamble = set()
n = len(array)
for i in range(const):
	preamble.add(array[i])

myval = 0

for i in range(const,len(array)):
	myval = array[i]
	test = False
	for j in range(i-const,i):
		if myval - array[j] in preamble:
			test = True
			continue
	if test == False:
		print("part 1:" + str(myval))
		for k in range(0,i):
			arr2 = []
			for l in range(k,i):
				if sum(arr2) + array[l] <= myval:
					arr2.append(array[l])
					if sum(arr2) == myval:
						print("part 2: " + str(max(arr2) + min(arr2)))
						print(str(max(arr2)),str(min(arr2)))

		break
	preamble.remove(array[i-const])
	preamble.add(array[i])

