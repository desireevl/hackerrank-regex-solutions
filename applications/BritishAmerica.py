import re
n = int(input())
w = ''
for i in range(n):
    w += input().strip()
t = int(input())
wr = []
for i in range(t):
    wr.append(input().strip())
for i in wr:
    j = i[:-2]
    if i[-2] =='z':
        j+='se'
    else:
        j+='ze'
    print(w.count(i)+w.count(j))
