list1=[[1,2,4],[2,4,4],[1,2]]
i=0
n=[]
while i<len(list1):
    sum=0
    j=0
    while j<len(list1[i]):
        sum=sum+list1[j][i]
        j=j+1
    n.append(sum)
    i=i+1
print(n)