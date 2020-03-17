import sys
import re

tablica = []

sciezka = r'^5{3}-\d{3}-\d{3}$'
sciezka2 = r'^5{3}[" "]\d{3}[" "]\d{3}$'

for line in sys.stdin:
	line = line.rstrip('\n')
	dopasowanie = re.search(sciezka, line)
	dopasowanie2 = re.search(sciezka2, line)
	if (dopasowanie or dopasowanie2):
		tablica.append('yes')
	else:
		tablica.append('no')

for x in tablica:
	print(x)
