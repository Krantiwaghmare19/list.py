binary_number=[1,0,0,1,1,0,1,1]
n=len(binary_number)
i=0
sum=0
while i<n:
    sum=(2**i)*binary_number[n-1-i]
    i=i+1
print(sum)