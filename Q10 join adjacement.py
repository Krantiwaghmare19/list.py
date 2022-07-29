from tkinter import N


list1=["1","2","3","4","5","6","7","8"]
i=0
g=[]
while i<1:
    n=0
    j=1+n 
    while j<len(list1) and n<len(list1):
        sum=list1[n]+list1[j]
        g.append(sum)
        n=n+2
        j=j+2
    i=i+1
print(g)

list1=["kranti","waghmare","priti","kale","pratiksha","aagle","mayuri","virgat"]
i=0
g=[]
while i<1:
    n=0
    j=1+n
    while j<len(list1) and n<len(list1):
        sum=list1[n]+list1[j]
        g.append(sum)
        n=n+2
        j=j+2
    i=i+1
print(g)