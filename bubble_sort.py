A = [64, 25, 12, 22, 11]

for i in range(len(A)):

	for j in range (len(A)-1):
		if A[j] > A[j+1]:
			A[j], A[j+1] = A[j+1], A[j]

print (A)
