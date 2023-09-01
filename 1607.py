T = int(input())

for i in range(T):
    cont = 0
    A, B = input().split(' ')
    for j in range(len(A)):
        if A[j] == B[j]:
            continue
        else:
            while A[j] != B[j]:
                if (A[j] == 'z'):
                    A[j] = 'a'                   
                else:
                    num_letra = ord(A[j]) + 1
                    A[j] = chr(num_letra)
                cont += 1
            
    print(cont)    
        
    