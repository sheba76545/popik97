A = [int(line) for line in open ('17-4.txt')]
B = [A[i]+A[i+1] for i in range(len(A)-1) if ((A[i]+A[i+1])%3==0) and ((A[i]+A[i+1])%6!=0)]
print(len(B),max(B))