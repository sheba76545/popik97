A=[int(line) for line in open('17-5.txt')]
B=[A[i]+A[i+1] for i in range(len(A)-1) if (A[i]+A[i+1])%2==0 and (A[i]+A[i+1])%6!=0]
print(len(B),max(B))