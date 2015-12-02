# MindT

n - количество переменных (a, b, c, ...)
m - максимальное значение переменной


commands
0   add a, b        [a] := [a] + [b]
1   mul a, b        [a, b] := [a] * [b]
2   inc a           [a] := [a] + 1 
3   mov a, b        [a] ;= [b]
4   xchg a, b       [a], [b] := [b], [a]


Например:

a   b   c   d
10  12  14  99

mul a, c
inc d

a   b   c   d
1   12  41  0

(d стало равно 100, так что 1 перенеслась в c)
