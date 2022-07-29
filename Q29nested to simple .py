list1=[[2,4,3],[1,5,6,],[7,9,0]]
i=0
b=[]
while i<len(list1):
    j=0
    while j<len(list1[i]):
        b.append(list1[i][j])
        j=j+1
    i=i+1
print(b)