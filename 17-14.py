text = [int(line) for line in open('17-14.txt')]
testt = [text[i] for i in range(len(text)) if (str(text[i])[-1]) == '7']
test = min(testt)
answ = [text[i] + text[i+1] for i in range(len(text)-1) if ((((str(text[i])[-1]) == '7')
        and ((str(text[i+1])[-1]) != '7')) or (((str(text[i])[-1]) != '7')
        and ((str(text[i+1])[-1]) == '7'))) and (((text[i] + text[i+1]) ** 2) >= (test ** 2))]
print(len(answ), max(answ) ** 2)
