# list=[6,1,3,5,3,1]
# i=0
# num=1
# g=[]
# while i<len(list):
#     if list[i] not in g:
#         g.append(list[i])
#         num=list[i]*num
#     i=i+1
#     print(num)

list=[6,1,3,5,3,1]
i=0
num=1
g=[]
while i<len(list):
    if list[i] not in g:
        g.append(list[i])
        num=list[i]*num
    i=i+1
    print(num)
