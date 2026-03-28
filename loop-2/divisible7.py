a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)