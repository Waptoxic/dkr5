def f(n):
    maxx(n)
    for i in range(len(n) - 1, 0, -1):
        n[0], n[i] = n[i], n[0]
        maxzn(n, s=0, v=i)
def parent(i):
    return (i - 1)//2
def lt(i):
    return 2*i + 1 
def rt(i):
    return 2*i + 2
def maxx(n):
    length = len(n)
    start = parent(length - 1)
    while start >= 0:
        maxzn(n, s=start, v=length)
        start = start - 1
 
def maxzn(n, s, v):
    l = lt(s)
    r = rt(s)
    if (l < v and n[l] > n[s]):
        naib = l
    else:
        naib = s
    if (r < v and n[r] > n[naib]):
        naib = r
    if (naib != s):
        n[naib], n[s] = n[s], n[naib]
        maxzn(n, naib, v)
 
 
n =[int(x) for x in open('rt.txt')]
f(n)
import json
with open('nigga.txt','w') as f:
    json.dump(n,f)
print('сортированный список: ', end='')
print(n)
