A=[int(x) for x in open('17-2.txt')]
B=[A[i]+A[i+1] for i in range(len(A)-1) if (A[i]%2==1 and A[i+1]%2==1) and ((A[i]+A[i+1])//2 in A) ]
print(len(B),max(B)//2)
