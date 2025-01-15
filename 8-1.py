from itertools import*
letters = 'изучатй'
comb = product(letters, repeat = 7)
k = 0
for words in comb:
    w = ''.join(words)
    if ((w.count('и') == 1) and (w.count('з') == 1) and (w.count('у') == 1) and (w.count('ч') == 1) and (w.count('а') == 1) and (w.count('т') == 1) and (w.count('й') == 1)) and (w[0] != 'й') and (('ии' not in w) and ('иа' not in w) and ('аи' not in w) and ('иу' not in w)and ('уи' not in w)and ('уу' not in w) and ('ау' not in w) and ('уа' not in w) and ('йт' not in w) and ('тт' not in w) and ('тй' not in w)) and ('тч' not in w) and ('зч' not in w) and ('зт' not in w) and ('зй' not in w) and ('зз' not in w)and ('чз' not in w) and ('тз' not in w) and ('йз' not in w) and ('чт' not in w) and ('чй' not in w) and ('чч' not in w) and ('йч' not in w) and ('йй' not in w):
        k+=1
        print(k, w)