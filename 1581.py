n = int(input())
for i in range(n):
    k = int(input())
    lingua = input()
    for j in range(k-1):
        if lingua != input():
            lingua = "ingles"
            break
    print(lingua)