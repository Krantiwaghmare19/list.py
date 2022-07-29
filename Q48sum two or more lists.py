# list1=[[1],[2,4,4],[1,2],[4]]
# i=0
# n=[]
# while i<len(list1):
#     sum=0
#     j=0
#     while j<len(list1[i]):
#         sum=sum+list1[i][j]
#         j=j+1
#     n.append(sum)
#     i=i+1
# print(n)

list1=[[2,3],[1,2,34],[5,6,7,8],[45,5,67,6],[9,7,78]]
i=0
n=[]
while i<len(list1):
    sum=0
    j=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j=j+1
    n.append(sum)
    i=i+1
print(n)