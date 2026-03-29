n=int(input("Enter the number of terms:"))
a=int(input("Enter the first term:"))
d=int(input("Enter the common difference:"))

for i in range(n):
    term=a+i*d
    print(term,end=" ")
