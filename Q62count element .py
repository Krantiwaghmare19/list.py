list=[2,3,1,5,10,7]
i=0
n=[]
while i<len(list):
    count=0
    j=i
    while j<len(list):
        if list[i]<list[j]:
            count=count+1
        j=j+1
    n.append(count)
    i=i+1
print(n)

print("kranti"*5)