num = int(input("Enter a Number : "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    cube = digit**order
    sum = sum + cube
    temp //= 10
if sum == num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")
