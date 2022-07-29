list=[5,6,[],3,[],[],9]
i=0
g=[]
n=[]
while i<len(list):
    if n!=list[i]:
        g.append(list[i])
    i=i+1
print(g)

list=[5,"kranti",[],"kamu",[],3,[]]
i=0
g=[]
n=[]
while i<len(list):
    if n!=list[i]:
        g.append(list[i])
    i=i+1
print(g)
