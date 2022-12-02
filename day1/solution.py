f = open("InputDay1.txt");

elfMap = {}
elfCounter = 0
elfMap[elfCounter] = 0
for line in f.readlines():
	if line == '\n':
		elfCounter+=1
		elfMap[elfCounter] = 0
	else:
		elfMap[elfCounter] = elfMap[elfCounter] + int(line)


print(sum(sorted(list(elfMap.values()))[-3:]))