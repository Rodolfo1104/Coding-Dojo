from collections import Counter

N = int(input())

for i in range(N):
    txt = input()
    d = Counter(txt.lower())
    for j in d.keys:
        if(not j.isalpha()):
            
