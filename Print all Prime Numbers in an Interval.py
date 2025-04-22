lower = int(input("Enter a lower Number : "))
upper = int(input("Enter a upper Number : "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(f"{num} is Prime Number")
