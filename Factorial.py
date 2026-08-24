def factorial(n):
    result = 1
    # Loop from 1 to n
    for i in range(1, n + 1):
        result = result * i
    return result

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    ans = factorial(num)
    print("The factorial of", num, "is:", ans)