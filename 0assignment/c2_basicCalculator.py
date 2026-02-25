n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Enter what operation you would like to perform: ")

result = 0

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "/":
    result = n1 / n2
elif operator == "*" or operator == "x":
    result = n1 * n2
else:
    print("please enter a valid operator")

print(n1, operator, n2, "=", result)
