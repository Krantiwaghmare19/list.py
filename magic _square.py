magic_square=[[8,3,4],
[1,5,9],
[6,7,2]]
row_sum=0
i=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        row_sum+magic_square[i][j]
        j=j+1
    i=i+1
    print(row_sum)
    print()
i=0
col_sum=0
while i<len(magic_square):
    j=0
    while i<len(magic_square):
        col_sum+=magic_square[i][j]
        j=j+1
        print(col_sum)
        print()
i=0
left_diagonal=0
while i<len(magic_square):
    left_diagonal+magic_square[i][j]
    i=i+1
    print(left_diagonal)
j=2
i=0
right_diagonal=0
while i<len(magic_square):
    right_diagonal+=magic_square[i][j]
    i=i+1
    j=j-1
print(right_diagonal)
print()
print(row_sum,col_sum,left_diagonal,right_diagonal)
if row_sum==col_sum and left_diagonal==right_diagonal:
    print("it is a magic square",row_sum,col_sum,left_diagonal,right_diagonal)
else:
    print("it is not magic square",row_sum,col_sum,left_diagonal,right_diagonal)




# a=[[8,3,4],
#    [1,5,9],
#    [6,7,2]]
# i=0
# while i<len(a):
#     s=0
#     j=0
#     while j<len(a[i]):
#         s=s+a[i]
#         j=j+1
#     i=i+1
#     print(s)
# x=0
# while x<len(a):
#     s1=0
#     y=0
#     while y<len(a[x]):
#         s1=s1+a[x][y]
#         y=y+1
#     x=x+1
#     print(s1,end="")
# print()
# if s==s1:
#     print("magic square")
# else:
#     print("not magic square")