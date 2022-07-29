list1=[23,46,32,25,46,33,71,90]
i=0
b=[]
h=[]
while i<len(list1):
    if list1[i]%2==0:
        b.append(list1[i])
    elif list1[i]%2!=0:
        h.append(list1[i])
print(b)

