list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
i=0
b=[]
while i<len(list1):
    if list1[i]>12 and list1[i]<18:
        b.append(list1[i])
    i=i+1
print(b)
