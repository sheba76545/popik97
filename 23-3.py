n = 10
K = [0] * (2*n)
K[10] = 1
for i in range(n-1, 0, -1):
    K[i] = K[i+1] + K[i*2]
print(K[1])