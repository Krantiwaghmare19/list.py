a=[99,2,2,23,19,23,11,1,3,4,78]
i=0
max=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    i=i+1
i=0
min=0
while i>len(a):
    if min>a[i]:
        min=a[i]
    i=i+1
print(max,"+",min,"=",max+min)
