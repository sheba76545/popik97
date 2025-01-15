F=open('24-1.txt', 'r')
st=F.readline()
ln=1
mxln=0
s=st[0]
for i in range (1,len(st)):
  if st[i]<st[i-1]:#проверка двух соседних символа(случай с обратным алфавитным порядком)
    ln+=1
    if ln>mxln: #поиск максимального значения
      mxln=ln
  else:
    ln=1 #обновление счётчика
    s=st[i]
print (mxln)