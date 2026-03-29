x=int(input("Enter the value of x:"))
n=int(input("Enter number of terms:"))
sum=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    term=x**i/fact
    if i%2==0:
        sum-=term
    else:
        sum+=term
print(sum)
