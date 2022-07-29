# numbers=[3,5,7,34,28,89,2,5]
# i=0
# max=0
# min=numbers[0]
# while i<len(numbers):
#     if numbers[i]>max:
#         max=numbers[i]
#     if numbers[i]<min:
#         min=numbers[i]
#     i=i+1
# print(max+min) 

num=[1,2,3,4,5,5,4,3,2,1]
i=0
max=0
min=num[0]
while i<len(num):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
    i=i+1
print(max)
print(min)
print(max+min)