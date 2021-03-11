import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

G = nx.DiGraph()

nodes = []
terminal = []
next_node = []
map = {}

rule = input()

while rule:
    rules = rule.split(' ')
    nodes.append(rules[0])
    terminal.append(rules[1])
    next_node.append(rules[2])
    rule = input()
print(nodes, terminal, next_node)

for n in nodes:
    map[n] = {}

for i in range(len(nodes)):
    map[nodes[i]][terminal[i]] = []

for i in range(len(nodes)):
    map[nodes[i]][terminal[i]].append(next_node[i])

for key in map.keys():
    for t in set(terminal):
        if t not in map[key]:
            map[key][t] = []

print(map)

def nfa_to_dfa(nfa):
    t = len(set(terminal))
    new_states_list = []
    dfa = {}
    keys_list = list(list(nfa.keys())[0])
    path_list = list(nfa[keys_list[0]].keys())

    dfa[keys_list[0]] = {}

    for y in range(t):
        var = "".join(nfa[keys_list[0]][path_list[y]])   #creating a single string from all the elements of the list which is a new state
        dfa[keys_list[0]][path_list[y]] = var            #assigning the state in DFA table
        if var not in keys_list and var != '':                         #if the state is newly created 
            new_states_list.append(var)                  #then append it to the new_states_list
            keys_list.append(var)                        #as well as to the keys_list which contains all the states

    ###################################################

    # Computing the other rows of DFA transition table

    while len(new_states_list) != 0:                     #consition is true only if the new_states_list is not empty
        dfa[new_states_list[0]] = {}                     #taking the first element of the new_states_list and examining it
        for _ in range(len(new_states_list[0])):
            for i in range(len(path_list)):
                temp = []                                #creating a temporay list
                for j in range(len(new_states_list[0])):
                    temp += (nfa[new_states_list[0][j]][path_list[i]])  #taking the union of the states
                s = ""
                s = s.join(temp)                         #creating a single string(new state) from all the elements of the list
                if s not in keys_list and s != '':                   #if the state is newly created
                    new_states_list.append(s)            #then append it to the new_states_list
                    keys_list.append(s)                  #as well as to the keys_list which contains all the states
                dfa[new_states_list[0]][path_list[i]] = s   #assigning the new state in the DFA table

        new_states_list.remove(new_states_list[0])       #Removing the first element in the new_states_list
    return dfa
dfa = nfa_to_dfa(map)
print(dfa)

G.add_nodes_from(map.keys())
for key, value in map.items():
    for ter, non in value.items():
        for n in non:
            G.add_edge(key, n, label=' '+ter)
A = to_agraph(G)
A.layout('dot')
A.draw('nfa.png')

new_dfa = {}

for key, value in dfa.items():
    new_dfa[key] = {k:v for k, v in value.items() if v != ''}

print(new_dfa)


G_dfa = nx.DiGraph()
G_dfa.add_nodes_from(new_dfa.keys())
for key, value in new_dfa.items():
    for ter, non in value.items():
            G_dfa.add_edge(key, non, label=' '+ter)
A = to_agraph(G_dfa)
A.layout('dot')
A.draw('dfa.png')
