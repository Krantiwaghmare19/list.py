list1=[[0,1,2],[2,3,4],[3,4,5,6],[7,8,9,10,11],[12,13,14]]
i=0
n=[]
while i<len(list1):
    sum=0
    j=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j=j+1
    n.append(sum)
    i=i+1
print(n)