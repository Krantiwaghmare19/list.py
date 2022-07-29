# list=[23,46,32,25,46,33,71,90]
# i=0
# a=[]
# b=[]
# while i<len(list):
#     if list[i]%2==0:
#         a.append(list[i])
#     elif list[i]%2!=0:
#         b.append(list[i])
#     i=i+1
# print([a,b])

list=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
i=0
a=[]
b=[]
while i<len(list):
    if list[i]%2==0:
        a.append(list[i])
    elif list[i]%2!=0:
        b.append(list[i])
    i=i+1
print([a,b])