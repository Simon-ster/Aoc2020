lines = []
f=open("input.txt")
for line in f.readlines():
	lines.append(line.strip())
#lines = [line.rstrip('\n') for line in f]
col = len(lines[0]) 
row = len(lines) 


def checkSeats(i,j):
	jj = [1,0,-1]
	ii = [1,0,-1]
	occ = 0
	for xx in ii:
		for yy in jj:
			if not (xx == 0 and yy == 0):
				x = i + xx
				y = j + yy
				if 0 <= x < row and 0 <= y < col:
					if lines[x][y] == '#':
						occ += 1
	return occ

def checkSeats2(i,j):
	jj = [1,0,-1]
	ii = [1,0,-1]
	occ = 0
	for xx in ii:
		for yy in jj:
			if not (xx == 0 and yy == 0):	
				x = i + xx
				y = j + yy
				while 0 <= x < row and 0 <= y < col and lines[x][y] == '.':
						x += xx
						y += yy
				if 0 <= x < row and 0 <= y < col:
					if lines[x][y] == '#':
							occ += 1
	return occ

cont = True
val = 0
while cont:
	next_layout = []	
	cont = False
	#print(row)
	#print(col)
	for i in range(row):
		string = ""
		for j in range(col):
			char = lines[i][j]
			if lines[i][j] == 'L' and checkSeats2(i,j) == 0:
				char = '#'	
				cont = True
			elif lines[i][j] == '#' and checkSeats2(i,j) >= 5:
				char = 'L'
				cont = True
			string += char
		next_layout.append(string)	
	#print(lines)
	#print(next_layout)
	if cont:
		lines = [p[:] for p in next_layout]
		#print(next_layout)

count = 0
for i in range(row):
	for j in range(col):
		if lines[i][j] == '#':
			count += 1
#print(lines)
print(count)
