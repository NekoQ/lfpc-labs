### Run
```bash
python.exe parse.py
```

### Result
```bash
{'S': ['dB'], 'B': ['C', 'CcB'], 'C': ['bA'], 'A': ['a', 'aA']}

Parse Table
    d   b   a  $   c
S  dB               
B      CY           
C      bA           
A          aZ       
Z           A  $   $
Y              $  cB

S
dB
dCY
dbAY
dbaZY
dbaY
dbacB
dbacCY
dbacbAY
dbacbaZY
dbacbaAY
dbacbaaZY
dbacbaaAY
dbacbaaaZY
dbacbaaaY
dbacbaaa

```
Derivation tree in the 'derivation.png' file
