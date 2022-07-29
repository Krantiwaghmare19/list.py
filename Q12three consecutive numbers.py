list1=[1,1,1,64,23,64,22,22,22]
i=0
n=[]
while i<len(list1):
    count=1
    j=1+i
    while j<len(list1):
        if list1[i]==list1[j]:
            count=count+1
        j=j+1
    if count==3:
        if list1[i] not in n:
            n.append(list1[i])
    i=i+1
print(n)    


list1=["kranti","kranti","kranti","priti","priti","priti","kamu","kamu","kamu","ty","yu","ty","ty","sa"]
i=0
n=[]
while i<len(list1):
    count=1
    j=1+i
    while j<len(list1):
        if list1[i]==list1[j]:
            count=count+1
        j=j+1
    if count==3:
        if list1[i] not in n:
            n.append(list1[i])
    i=i+1
print(n)

