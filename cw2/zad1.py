import sys

przejscia = dict()
stanKoncowy = []

for line in sys.stdin:
    line = line.split()
    if(len(line) == 1):
        stanKoncowy.append(line[0])
    elif(len(line) == 3):
        if((int(line[0]), line[2])) not in przejscia:
            przejscia[(int(line[0]), line[2])] = line[1]


def sprawdzenie(slowo):
    stanPoczatkowy = 0
    tablicaSlowa = list(slowo)
    for x in tablicaSlowa:
        if ((stanPoczatkowy, x)) in przejscia:
            przejscie = przejscia[(stanPoczatkowy, x)]
            stanPoczatkowy = int(przejscie)
        else:
            print("FALSE " + slowo)
            return False
    if str(stanPoczatkowy) in stanKoncowy:
        print("TRUE " + slowo)
    else:
        print("FALSE " + slowo)


with open(sys.argv[1]) as file:
    for line in file:
        line = line.rstrip("\n")
        sprawdzenie(line)
