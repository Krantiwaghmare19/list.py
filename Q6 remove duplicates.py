# list=[1,2,3,1,2,2]
# i=0
# g=[]
# while i<len(list):
#     if list[i] not in g:
#         g.append(list[i])
#     i=i+1
# print(g)


# list=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
# i=0
# g=[]
# while i<len(list):
#     if list[i] not in g:
#         g.append(list[i])
#     i=i+1
# print(g)

list=[1,2,3,4,5,6,6,5,4,3,2,1]
i=0
g=[]
while i<len(list):
    if list[i]not in g:
        g.append(list[i])
    i=i+1
print(g)