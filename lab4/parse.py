from pandas import DataFrame
from copy import deepcopy
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

map = {}

f = open('grammar.txt', 'r')

for line in f:
    s = line.split('-')
    map[s[0]] = []

f.seek(0)
for line in f:
    s = line.split('-')
    map[s[0]].append(s[1][:-1])

print(map)

# Remove left recursion
mapCopy = deepcopy(map)
for key, value in mapCopy.items():
    for v in value:
        if key == v[0]:
            new = v[1:]
            map['X'] = [new, new+'X']
            map[key].remove(v)
            map[key] += [i+'X' for i in map[key]]

# Remove left factoring
chars = ['Y', 'Z', 'W', 'Q']
next = 0
mapCopy = deepcopy(map)
for key, value in mapCopy.items():
    if len(value) > 1 and value[0][0] == value[1][0]:
        map[key].clear()
        map[key].append(value[0][0]+chars[next])
        map[chars[next]] = [v.replace(value[0][0], '') for v in value]
        next += 1

first = {}
follow = {}
parse = {}

for key in map.keys():
    first[key] = []
    follow[key] = []
    parse[key] = {}

for key in map.keys():
    # First
    next = key
    exists = True
    while exists:
        exists = False
        for non in map[next]:
            if non == '':
                first[key].append(non)
            elif non[0] not in map.keys():
                first[key].append(non[0])
            else:
                exists = True
                next = non[0]
for key in map.keys():
    for value in map.values():
        for v in value:
            if key in v:
                following = v.find(key)+1
                if following == len(v):
                    pass
                elif v[following] in map.keys():
                    follow[key] += [i for i in first[v[following]] if i != '']
                elif key != v[-1]:
                    follow[key].append(v[following])

for gKey in map.keys():
    for key, value in map.items():
        for v in value:
            if gKey in v and gKey == v[-1] and gKey != key:
                follow[gKey] += follow[key]

# Parse Table
for key, value in map.items():
    for v in value:
        if v == '':
            parse[key]['$'] = '$'
            for f in follow[key]:
                parse[key][f] = '$'
        elif v[0] not in map.keys():
            parse[key][v[0]] = v
        else:
            for f in first[v[0]]:
                parse[key][f] = v

print("\nParse Table")
print(DataFrame.from_dict(parse, orient='index').fillna(''), end='\n\n')

stack = ['S']

word = open('string.txt', 'r').readline().replace('\n', '$')
newWord = 'S'
print(newWord)

G = nx.DiGraph()
G.add_node(1, label='S')
nodeNumber = 1

while word[0] != '$' or stack[0] != '$':
    char = stack.pop()
    letter = word[0]

    if char == '$':
        continue
    if char == letter:
        word = word[1:]
        continue
    newChars = list(parse[char][letter])
    newWord = newWord.replace(char, parse[char][letter]).replace('$', '')
    print(newWord)
    stack += reversed(newChars)


    for n in G.nodes():
        if G.nodes[n]['label'] == char:
            parent = n
    for n in newChars:
        nodeNumber += 1
        G.add_node(nodeNumber, label=n)
        G.add_edge(parent, nodeNumber)

A = to_agraph(G)
A.layout('dot')
A.draw('derivation.png')
