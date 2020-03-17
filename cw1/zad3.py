import sys
import re

tablica = []

sciezka = r'^(os|ul|al)\.[" "][A-ZĆŁŚŹŻ]{1}[a-zżźćńółęąś]+[" "][1-9]+(|[" "]m.[" "][1-9]+)$'
sciezka2 = r'^(os|ul|al)\.[" "][A-ZĆŁŚŹŻ]{1}[a-zżźćńółęąś]+[" "][1-9]+\/[1-9]+$'

for line in sys.stdin:
    line = line.rstrip('\n')
    dopasowanie = re.search(sciezka, line)
    dopasowanie2 = re.search(sciezka2, line)
    if dopasowanie:
        result = line.split(" ")
        tablica.append(result[2])
    elif dopasowanie2:
        tmp = line.split(" ")
        result = tmp[2].split("/")
        tablica.append(result[0])
    else:
        tablica.append('<NONE>')

for x in tablica:
    print(x)
