n=int(input("Enter the number of terms:"))
a=int(input("Enter the first term:"))
r=int(input("Enter the common ratio:"))

for i in range(1,n+1):
    term=a*(r*i)
    print(term,end=" ")