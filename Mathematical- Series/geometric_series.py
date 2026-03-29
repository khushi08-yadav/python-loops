x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
sum=0
for i in range(0,n+1):
    sum+=x**i
print("The sum of the geometric series is :",sum)