# a=[1,2,3,[4,5,6,],[7,8,9,10]]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if (type(a[i]))==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         b.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(sum)

# a=[1,3,56,[32,33,44,3,21],[2,4,5,2,8,9,7,6]]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if (type(a[i]))==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         b.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(sum)

a=[1,2,3,4,5,6,2,3,4]
i=0
sum=0
b=[]
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(sum)


# l=[[[[[[1]]]]]]
# for a in l:
#     for b in a:
#         for c in b:
#             for d in c:
#                 for e in d:
#                     for f in e:
#                         print((f))


# list=[]
# for i in range(0,8):
#     if i%2==0:
#         list.append(i**2)
#     else:
#         list.append(i**3)
# print(list)

# list=[0,1,2,3,4,5,6,7,8]
# g=[]
# i=0
# while i<len(list):
#     if i%2==0:
#         g.append(i**2)
#     else:
#         g.append(i**3)
#     i=i+1
# print(g)

list=[0,1,2,3,4,5,6,7,8]
i=0
g=[]
h=[]
while i<len(list):
    if i%2==0:
        g.append(i**2)
    else:
        h.append(i**3)
    i=i+1
print([g,h])
