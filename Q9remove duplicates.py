list1=[1,2,4,6,3,6,8,4,7,4,8995,7,9,56]
i=0
g=[]
while i<len(list1):
    if list1[i] not in g:
        g.append(list1[i])
    i=i+1
print(g)
        

list1=[1,2,3,4,5,6,1,3,2,3,4,5]
i=0
g=[]
while i<len(list1):
    if list1[i]not in g:
        g.append(list1[i])
    i=i+1
print(g)