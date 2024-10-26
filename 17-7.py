A=[int(line) for line in open('17-7.txt')]
B=[A[i]+A[i+1] for i in range(len(A)-1) if (A[i]%5==0 or A[i+1]%5==0) and ((A[i]+A[i+1])%10!=0) and (A[i]+A[i+1]) in A ]
print(len(B),max(B))