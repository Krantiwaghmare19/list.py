list1=['aabc','abc','ab','ha']
b=str(list1[0])
a=b[0]
i=0
count=0
while i<len(list1):
    c=str(list1[i])
    if c[0]==a:
        count=count+1
    i=i+1
if count==len(list1):
    print("True")
else:
    print("False")



list1=['aabc','abc','ab','a']
b=str(list1[0])
a=b[0]
i=0
count=0
while i<len(list1):
    c=str(list1[i])
    if c[0]==a:
        count=count+1
    i=i+1
if count==len(list1):
    print("True")
else:
    print("False")
    