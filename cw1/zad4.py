import sys
import re

tablica = []

sciezka = r'^[A-ZĆŁŚŹŻ]{1}[a-zżźćńółęąś]*[a][" "][A-ZĆŁŚŻŹ]{1}[a-zżźćńółęąś]+$'

for line in sys.stdin:
    line = line.rstrip('\n')
    dopasowanie = re.search(sciezka, line)
    result = line.split(" ")
    if result[0] == 'Kosma' or result[0] == 'Jarema':
        tablica.append('<NONE>')
    elif dopasowanie:
        tablica.append(result[1])
    else:
        tablica.append('<NONE>')

for x in tablica:
    print(x)
