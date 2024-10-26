A=[int(line) for line in open('17-6.txt')]
B=[A[i]+A[i+1]+A[i+2] for i in range(len(A)-2) if A[i] < A[i+1] < A[i+2]]
print(len(B),max(B))
