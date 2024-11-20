s=[x for x in range(1043,7238) if (x%4==0) and (x%12!=0 and x%16!=0 and x%25!=0)]
print(len(s),s)