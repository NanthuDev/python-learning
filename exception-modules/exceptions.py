number = 10
result = number / 3

print(result)


try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

print("Program continues...")

