A = [64, 25, 12, 22, 11]
 
for i in range(len(A)):

    min_p = i
    for j in range(i+1, len(A)):
        if A[min_p] > A[j]:
            min_p = j

    A[i], A[min_p] = A[min_p], A[i]
 
print(A)
