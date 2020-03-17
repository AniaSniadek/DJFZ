import sys

tablica = []
spacja = " "

for line in sys.stdin:
	line = line.rstrip('\n')
	count = len(line)
	result = str(count) + spacja + line
	tablica.append(result)

for x in tablica:
	print(x)
