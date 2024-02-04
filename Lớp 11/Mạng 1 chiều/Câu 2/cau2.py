import random
from sys import path
from os.path import join
inp = join(path[0],'cau2.inp')
with open(inp,'r') as i:
    v = i.readlines()
out = join(path[0],'cau2.out')
n = int(v[0])
l = list(map(int, v[1].split()))
for i in range(n):
    if l[i] == max(l):
        p = i + 1
        break
with open(out,'w') as o:
    o.write(f'{max(l)}\n{p}')