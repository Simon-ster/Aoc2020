array = []
i = 0
with open("input4.txt",'r') as input:
    array.append("_")
    for line in input.readlines():
        array[i]+=line.strip()
        if line == "\n":
            i += 1
            array.append("_")

test = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count = 0
bad = set()
for i in array:
    count += 1
    for j in test:
        if j not in i:
            if i not in bad:
                print(i,j)
                bad.add(i)
                count -= 1

print(count)