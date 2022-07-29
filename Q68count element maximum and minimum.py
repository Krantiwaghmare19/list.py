# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# l=len(list)
# i=0
# max_list=list[0]
# min_list=list[0]
# while i<len(list):
#     if len(list[i])<len(min_list):
#         min_list=list[i]
#     if len(list[i])>len(max_list):
#         max_list=list[i]
#     i=i+1
# print(len(max_list),max_list)
# print(len(min_list),min_list)

list=[[1],[2,3],[1,2,3],[7,6,88,33],[77,3,4,6,67]]
l=len(list)
i=0
max_list=list[0]
min_list=list[0]
while i<len(list):
    if len(list[i])<len(min_list):
        min_list=list[i]
    if len(list[i])>len(max_list):
        max_list=list[i]
    i=i+1
print(len(max_list),max_list)
print(len(min_list),min_list)