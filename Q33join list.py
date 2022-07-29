list1=[[10,20],[30,40],[50,60],[30,20,80]]
list2=[[61],[12,14,15],[12,13,19,20],[12]]
i=0
n=[]
while i<len(list1):
    h=list1[i]+list2[i]
    n.append(h)
    i=i+1
print(n)