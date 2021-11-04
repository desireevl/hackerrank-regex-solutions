import re
n = int(input())
sentences=[]
for i in range(n):
    sentences.extend(list(input().split()))
t = int(input())
for i in range(t):
    word = input()
    bword = re.sub("our","or",word)
    count=0
    for each in sentences:
        if word==each or bword ==each:
            count+=1
    print(count)
