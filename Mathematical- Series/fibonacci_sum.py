n=int(input("Enter the number of terms:"))
a,b=0,1
sum=0

for i in range(n):
    sum+=a
    temp=a+b
    a=b
    b=temp
print("The sum of the fibonacci series is:",sum)
