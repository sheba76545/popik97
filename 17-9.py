a=[int(line) for line in open('17-9.txt')]
b=[a[i]+a[i+1] for i in range(len(a)-1) if ((str(a[i]))[-1]=='7') or ((str(a[i+1]))[-1]=='7')]