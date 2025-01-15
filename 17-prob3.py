f = [int(line) for line in open('17-12.txt')]
f1 = [f[i] for i in range(len(f)) if str(f[i])[-1] == '3']
a = abs(min(f1))
f2 = [f[i]+f[i+1] for i in range(len(f)-1) if ((str(f[i])[-1] == '3' and str(f[i+1])[-1] != '3')
      or (str(f[i])[-1] != '3' and str(f[i+1])[-1] == '3')) and (((int(f[i])+int(f[i+1]))**2) >= a)]
print(len(f2), max(f2)**2)
print(f2)
