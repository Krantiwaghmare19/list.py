list1=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
k=4
n=[]
i=0
while i<len(list1):
    if i==k:
        n.append(20)
        k=k+4
    n.append(list1[i])
    i=i+1
print(n)