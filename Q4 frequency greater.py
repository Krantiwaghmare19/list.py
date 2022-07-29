list1=[4,6,4,3,3,4,3,4,3,8]
i=0
n=[]
while i<len(list1):
    j=0
    count=0
    while j<len(list):
        if list1[i]==list1[j]:
            count=count+1
            j=j+1
    if count>2:
        if list1[i] not in n:
            n.append(list1[i])
    i=i+1
print(n)

# list1=[4,6,4,3,3,4,3,4,3,8]
# i=0
# n=[]
# while i<len(list1):
#     j=0
#     count=0
#     while j<len(list):
#         if list1[i]==list1[j]:
#             count=count+1
#             j=j+1
#     if count>2:
#         if list1[i] not in n:
#             n.append(list1[i])