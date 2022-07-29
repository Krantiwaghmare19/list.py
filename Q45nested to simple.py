list1=[1,[2,[2,3],[3],4]]
i=0
n=[]
while i<len(list1):
    if type(list1[i])==list1:
        j=0
        while j<len(list1[i]):
            if type(list1[i][j])==list1:
                print(list1[i][j])
                pass
            else:
                n.append(list1)
        j=j+1
    i=i+1
print(n)