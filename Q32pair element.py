list1=[1,2,3,4,5,6]
i=0
n=[]
while i<len(list1)-1:
    h=[list1[i],list1[i+1]]
    n.append(h)
    i=i+2
print(n)

