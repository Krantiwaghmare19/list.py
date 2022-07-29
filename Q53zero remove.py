list1=[1,0,5,0,7,0,8,0]
i=0
b=[]
while i<len(list1):
    if list1[i]==0:
        pass
    else:
        b.append(list1[i])
    i=i+1
print(b)