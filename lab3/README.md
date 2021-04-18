### Run
```bash
python.exe cfg_to_cnf.py
```
### Input
```bash
S AC
S bA
A bS
A BC
A AbC
B CbaC
B a
B bSa
C
D AB

```

### Result
```bash
S -> AC | bA 
A -> bS | BC | AbC 
B -> CbaC | a | bSa 
C ->  
D -> AB 

After null elimination:
S -> A | bA 
A -> bS | B | Ab 
B -> ba | a | bSa 
D -> AB 

After unit production removal:
S -> bA | bS | Ab | ba | a | bSa 
A -> bS | Ab | ba | a | bSa 
B -> ba | a | bSa 
D -> AB 

After nonproductive elimination:
S -> bA | bS | Ab | ba | a | bSa 
A -> bS | Ab | ba | a | bSa 
B -> ba | a | bSa 
D -> AB 

After inaccesible elimination:
S -> bA | bS | Ab | ba | a | bSa 
A -> bS | Ab | ba | a | bSa 

After removing more than 2 variables:
S -> bA | bS | Ab | ba | a | bY1 
A -> bS | Ab | ba | a | bY1 
Y1 -> Sa 

Chomsky Normal Form:
S -> X1A | X1S | AX1 | X1X2 | a | X1Y1 
A -> X1S | AX1 | X1X2 | a | X1Y1 
Y1 -> SX2 
X1 -> b 
X2 -> a
```