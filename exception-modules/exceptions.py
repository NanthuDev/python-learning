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



try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Calculation successful:", result)

finally:
    print("Calculation attempt finished.")




def deposit(amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")

    print(f"Deposited: {amount}")


deposit(500)
# deposit(-100)


try:
    result = deposit(-100)
    print(result)

except ValueError as error:
    print("Deposit failed:", error)
