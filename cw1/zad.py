import sys

tablica = []
space = " "

for line in sys.stdin:
	line = line.rstrip('\n')
	count = len(line)
	result = str(count) + space + line
	tablica.append(result)

for x in tablica:
	print(x)
