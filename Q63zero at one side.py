list=[1,0,3,4,5,7,0,9]
n=[]
i=0
while i<len(list):
    if list[i]!=0:
        n.append(list[i])
    i=i+1
j=0
while j<len(list):
    if list[j]==0:
        n.append(list[j])
    j=j+1
print(n)


list=[1,0,2,0,3,0,4,0,5,0,6,0,7,0]
n=[]
i=0
while i<len(list):
    if list[i]!=0:
        n.append(list[i])
    i=i+1
j=0
while j<len(list):
    if list[j]==0:
        n.append(list[j])
    j=j+1
print(n)
