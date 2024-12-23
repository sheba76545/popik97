f = open('24-8.txt')
text = f.read()
s = []
text = text.replace('DA', 'D A')
text = text.replace('AD', 'A D')
text = text.replace('BD', 'B D')
text = text.replace('DB', 'D B')
text = text.replace('CD', 'C D')
text = text.replace('DC', 'D C')
text = text.replace('ED', 'E D')
text = text.replace('DE', 'D E')
text = text.replace('FD', 'F D')
text = text.replace('DF', 'D F')
text = text.split()
w = [len(text[i]) for i in range(len(text)) if "D" not in text[i]]
print(max(w))


