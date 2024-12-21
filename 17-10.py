a = [int(line) for line in open('17-10.txt')]
c = [a[r] for r in range(len(a)) if (str(a[r])[-1]) == '7']
f = min(c)**2
b = [a[i]+a[i+1] for i in range(len(a)-1) if (((((str(a[i]))[-1]) != '7') and (((str(a[i+1]))[-1]) == '7')) or
     ((((str(a[i]))[-1]) == '7') and (((str(a[i+1]))[-1]) != '7'))) and (((a[i]+a[i+1])**2) >= f)]
print(len(b),max(b), (max(b))**2)
