# list1=[424,111,876,456]
# i=0
# while i<len(list1):
#     rev=0
#     a=list1[i]
#     while list1[i]>0:
#         rev=(rev*10)+list1[i]%10
#         list1[i]//=10
# if a==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
# i=i+1

# num=input("enter the word")
# n=num[-1::-1]
# print(n)
# if num==n:
#     print("palindrome:")
# else:
#     print("not palindrome")



# def a(lst,spec_index):
#     result = []
#     length = len(lst)
#     for i in range(length):
#         element_index = spec_index % length
#         result.append(lst[element_index])
#         spec_index += 1
#     return result

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print("Original list:")
# print(chars)
# spec_index = 3
# print(spec_index,":")
# print(a(chars,spec_index))
# spec_index = 5
# print(spec_index,":")
# print(a(chars,spec_index))