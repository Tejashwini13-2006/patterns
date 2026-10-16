num=[1,4,5,6,7,7,8,1,1,111,5,5,8,9,13,13]
d={}
for i in range(0,len(num)):
    if num[i] in d:
        d[num[i]]+=1
    else:
        d[num[i]]=1
print(d)