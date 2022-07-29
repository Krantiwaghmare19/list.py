from tkinter import N


list1=["1","2","3","3","2"]
i=0
g=[]
while i<1:
    n=0
    j=1+n
    while j<len(list1) and n<(len(list1)):
        sum=list1[n]+list1[j]
        g.append(sum)
        n=n+2
        j=j+2
    i=i+1
print(g)