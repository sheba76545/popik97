file = open(r"C:\Users\serba\Downloads\26-4.txt")
first_str = file.readline().split()
first_str = int(first_str[0])
users = sorted(int(line) for line in file)
summa = 0
i = 0
while summa <= first_str:
    summa += users[i]
    i += 1
print(i - 1)
summa -= users[i-1] + users[i]
avaliable = first_str - summa
m = [x for x in users if x <= avaliable]
#for k in range(i, len(users)):
#    if (users[k] <= avaliable) and (users[k] > m):
#       m = users[k]
print(max(m) )