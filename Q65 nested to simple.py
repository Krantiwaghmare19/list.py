a=[[1],[2],[2,6]]
i=0
b=[]
while i<len(a):
    j=0
    while i<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
