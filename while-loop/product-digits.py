n=int(input("Enter the number:"))
product=1

while n>0:
    digit=n%10
    product*=digit
    n//=10
#print the product of all digits of a given number
print(product)