import re
array = []
with open("input2.txt",'r') as input:
	for line in input.readlines():
		array.append(line.strip())

sol1 = []
sol2 = []

for i in array:
    arr = i.split(": ")
    vals = arr[0].split("-")
    lets = vals[1].split(" ")

    start = int(vals[0])
    end = int(lets[0])
    letter = lets[1]
    counter = arr[1].count(letter)

    if counter <= end and counter >= start:
        sol1.append(arr[1])
    if arr[1][start-1] == letter or arr[1][end-1] == letter:
        if arr[1][start-1] != arr[1][end-1]:
            sol2.append(arr[1])


print(len(sol1))
print(len(sol2))