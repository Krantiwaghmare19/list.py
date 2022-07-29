list1=["Red","Maroon","Yellow","Olive"]
i=0
n=[]
while i<len(list1):
    j=0
    h=[]
    while j<len(list1[i]):
        h.append(list1[i][j])
        j=j+1
    n.append(h)
    print()
    i=i+1
print(n)