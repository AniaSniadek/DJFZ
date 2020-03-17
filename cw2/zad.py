import re
import sys

sciezka = r'^\d+ \d+ [a-z](| \d+\.\d+)$'

numer = 0

for line in sys.stdin:
	dopasowanie = re.search(sciezka, line)
	if dopasowanie:
		numer+=1

print(numer)
