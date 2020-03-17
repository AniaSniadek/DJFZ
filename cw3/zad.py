import sys

przejscia = dict()
stanKoncowy = []
symbole = []

for line in sys.stdin:
    line = line.split()
    if(len(line) == 1):
        stanKoncowy.append(line[0])
    elif(len(line) == 3 or len(line) == 4):
        if line[2] not in symbole:
            symbole.append(line[2])
        if((int(line[0]), line[2])) not in przejscia:
            przejscia[(int(line[0]), line[2])] = line[1]

stanPoczatkowy = '0'
slowa = []
lista = []


def dfs(graph, node, visited):
    if str(node) in stanKoncowy:
        slowo = "". join(visited)
        slowa.append(slowo)
    for symbol in symbole:
        if ((int(node), symbol)) in graph:
            n = graph[int(node), symbol]
            lista = visited[:]
            lista.append(symbol)
            dfs(graph, int(n), lista[:])


dfs(przejscia, stanPoczatkowy, [])

slowa.sort()
for x in slowa:
    print(x)
