n=int(input("Enter a number:"))
count=0

while n>0:
    digits=n%10
    count+=digits
    n//=10
#print the count of all digits of a given number
print(count)