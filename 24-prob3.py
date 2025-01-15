f = open('24-12.txt')
text = f.read()
s = []
text = text.replace('AA', 'A A')
text = text.replace('AE', 'A E')
text = text.replace('EA', 'E A')
text = text.replace('EE', 'E E')
text = text.replace('BB', 'B B')
text = text.replace('BC', 'B C')
text = text.replace('BD', 'B D')
text = text.replace('CC', 'C C')
text = text.replace('CB', 'C B')
text = text.replace('CD', 'C D')
text = text.replace('DB', 'B B')
text = text.replace('DC', 'D C')
text = text.replace('DD', 'D D')
text = text.split()
for i in text:
    if ('A' == i[0]) or ('A' == i[0]):
        print(len(i), i)



