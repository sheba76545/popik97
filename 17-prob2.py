A=[int(line) for line in open('17-prob2.txt')]
C=[A[i] for i in range(len(A)) if A[i]%32==0]
B=[A[i]+A[i+1] for i in range(len(A)-1) if ((A[i]<0) or (A[i+1]<0)) and ((A[i]+A[i+1])<len(C))]
print(max(B),len(B),B)