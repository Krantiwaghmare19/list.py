# binary=[1,0,1,0]
# i=1
# c=0
# sum=0
# while i<=len(binary):
#     sum=(binary[-i]*2**c+sum)
#     c=c+1
#     i=i+1
# print(sum)

binary=[1,0,1,0,1,0,1,0,1]
i=1
c=0
sum=0
while i<len(binary):
    sum=(binary[-i]*2**c+sum)
    c=c+1
    i=i+1
print(sum)