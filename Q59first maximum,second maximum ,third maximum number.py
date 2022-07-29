list=[4,3,9,7,10,12,2,9,14]
i=0
a=0
while i<len(list):
    if list[i]>a:
        a=list[i]
    i=i+1
print(a)
i=0
b=0
while i<len(list):
    if list[i]>b:
        if list[i]!=a:
            b=list[i]
    i=i+1
print(b)
i=0
c=0
while i<len(list):
    if list[i]>c:
        if list[i]!=a and list[i]!=b:
            c=list[i]
    i=i+1
print(c)