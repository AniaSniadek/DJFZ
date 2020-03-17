import sys
import re

tablica = []
sciezka = r'^[A-Z]{5}[" "][A-Z]{4}$'

for line in sys.stdin:
    line = line.rstrip('\n')
    dopasowanie = re.search(sciezka, line)
    if dopasowanie:
        numer = ''
        for i in range(10):
            if line[i] == 'A' or line[i] == 'B' or line[i] == 'C':
                numer += '2'
            elif line[i] == 'D' or line[i] == 'E' or line[i] == 'F':
                numer += '3'
            elif line[i] == 'G' or line[i] == 'H' or line[i] == 'I':
                numer += '4'
            elif line[i] == 'J' or line[i] == 'K' or line[i] == 'L':
                numer += '5'
            elif line[i] == 'M' or line[i] == 'N' or line[i] == 'O':
                numer += '6'
            elif line[i] == 'P' or line[i] == 'Q' or line[i] == 'R' or line[i] == 'S':
                numer += '7'
            elif line[i] == 'T' or line[i] == 'U' or line[i] == 'V':
                numer += '8'
            elif line[i] == 'W' or line[i] == 'X' or line[i] == 'Y' or line[i] == 'Z':
                numer += '9'
            elif line[i] == ' ':
                numer += '0'
        if numer == '4677304323':
            tablica.append('no')
        else:
            tablica.append('yes')
    else:
        tablica.append('no')

for x in tablica:
    print(x)
