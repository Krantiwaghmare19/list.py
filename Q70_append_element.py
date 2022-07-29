list=[1,2,3]
i=0
count=0
list1=[]
while i<len(list):
    list1.append(list[i])
    if count==0:
        list1.append(10)
    count=count+1
    i=i+1
print(list1)


list=[1,2,3,4,"fugljf",3]
i=0
count=0
list1=[]
while i<len(list):
    list1.append(list[i])
    if count==4:
        list1.append(10)
    count=count+1
    i=i+1
print(list1)