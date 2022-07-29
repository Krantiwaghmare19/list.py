list=[34,67,12,-94.89,'python',0,'c#']
i=0
my_list=[]
while i<len(list):
    if type(list[i])==int:
        my_list.append(list[i])
    i=i+1
print(my_list)

list=[12,97,647,"woeure","eiure",0,2.2,2+3j]
i=0
g=[]
while i<len(list):
    if type(list[i])==int:
        g.append(list[i])
    i=i+1
print(g)