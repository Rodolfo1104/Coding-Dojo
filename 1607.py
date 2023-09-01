T = int(input())

for i in range(T):
    cont = 0
    A, B = input().split(' ')
    for j in range(len(A)):

        if A[j] == B[j]:
            continue
        else:
            val1 = ord(A[j]) - ord("a")
            val2 = ord(B[j]) - ord("a")
            cont += (val2 - val1) % 26
            
    print(cont)    
        
    