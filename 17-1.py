A=[int(x) for x in open('17-1.txt')]
max19=max([x for x in A if x%19==0])
B=[A[i]+A[i+1] for i in range(len(A)-1) if (A[i]>max19) or (A[i+1]>max19)]
s=len(B)
min_s=min(B)
print(s,min_s)




