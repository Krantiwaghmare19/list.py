# list=[4,5,5,5,3,8]
# i=0
# n=[]
# while i<len(list):
#     j=1
#     count=0
#     while j<len(list):
#         if list[i]==list[j]:
#             count=count+1
#         j=j+1
#     if count>=3:
#         if list[i] not in n:
#             n.append(list[i])
#     i=i+1
# print(n)

list=[4,5,5,5,3,8]
i=0
n=[]
while i<len(list):
    j=1
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    if count>=3:
        if list[i]not in n:
            n.append(list[i])
    i=i+1
print(n)