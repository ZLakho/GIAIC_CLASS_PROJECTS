def Sum ():
    a = int(input("Enter your first digit: "))
    b = int(input("Enter your second digit: "))
    sum = a + b
    return f"Your sum of {a} and {b} is {sum}"

result = Sum()
print(result)