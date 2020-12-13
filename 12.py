f=open('input.txt')
lines = [line.rstrip('\n') for line in f]

location = complex(0,0)
facing = complex(1,0)

waypoint = complex(10,1)
ship = complex(0,0)

def rotateLeft(z):
	x = z.real
	y = z.imag
	return complex(-y,x)

def rotateRight(z):	
	x = z.real
	y = z.imag
	return complex(y,-x)

for line in lines:
	instruction = line[0]
	value = int(line[1:])
	
	if instruction == 'N': 
		location += complex(0,value)
		waypoint += complex(0,value)
	if instruction == 'E': 
		location += complex(value,0)
		waypoint += complex(value,0)
	if instruction == 'S': 
		location += complex(0,-value)
		waypoint += complex(0,-value)
	if instruction == 'W': 
		location += complex(-value,0)
		waypoint += complex(-value,0)
	if instruction == 'F': 
		location += value * facing
		ship += waypoint * value
	if instruction == 'L': 
		for i in range(value//90):
			facing = rotateLeft(facing)
			waypoint = rotateLeft(waypoint)
	if instruction == 'R':
		for i in range(value//90):
			facing = rotateRight(facing)
			waypoint = rotateRight(waypoint)

print(abs(location.real)+abs(location.imag))
print(abs(ship.real)+abs(ship.imag))


