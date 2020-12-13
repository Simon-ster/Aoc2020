array = []
with open("input12.txt") as input:
	for line in input.readlines():
		array.append(line.strip())

coord = (0,0)
direction = [(0,1),(1,0),(0,-1),(-1,0)]
cards = ["N","E","S","W"]


for i in array:
    prevDir = "E"
    