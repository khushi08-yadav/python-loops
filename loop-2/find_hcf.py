a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
hcf=1
for i in range(a,b+1):
    if a%i==0 and b%i==0:
        hcf=i
print("The HCF of",a,"and",b,"is",hcf)
