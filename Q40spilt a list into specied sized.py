list1=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
k=0
i=0
n=[]
while i<len(list1):
    j=0
    h=[]
    while j<3 and k!=len(list1):
        h.append(list1[k])
        j=j+1
        k=k+1
    n.append(h)
    if k==len(list1):
        break
    i=i+1
print(n)