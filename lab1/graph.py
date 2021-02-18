import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

G = nx.DiGraph()

nodes = []
right = []
map = {}


def test(word):
    next_non = 'S'
    for i, terminal in enumerate(word):
        if terminal in map[next_non].keys():
            next_non = map[next_non][terminal]
            if next_non == '$' and (i == len(word) - 1):
                return True
            elif next_non == '$':
                return False
        else:
            return False
    return False


rule = input()
while rule:
    nodes.append(rule.split('->')[0])
    right.append(rule.split('->')[1])
    rule = input()
print(nodes, right)

for n in nodes:
    map[n] = {}

print(map)

for i in range(len(nodes)):
    non = list(right[i])[0]

    terminal = '$'

    if len(list(right[i])) == 2:
        terminal = list(right[i])[1]

    print(nodes[i], non, terminal)
    map[nodes[i]][non] = terminal

print(map)
G.add_nodes_from(map.keys())


for key, value in map.items():
    for ter, non in value.items():
        for n in non:
            G.add_edge(key, n, label=' '+ter)


A = to_agraph(G)
A.layout('dot')
A.draw('graph.png')

while 1:
    word = input()
    print(test(word))
