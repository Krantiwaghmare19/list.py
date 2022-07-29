list1=[6,1,3,5,6,3,1]
b=[]
i=0
while i<len(list1):
    if list1[i] not in b:
        b.append(list1[i])
    i=i+1
print(b)