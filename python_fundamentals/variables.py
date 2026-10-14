name = "Nantha"
age = 33


print(name)
print(age)

# Python variables aren't restricted to one type.

salary = 8500.50
is_developer = True

# None means there is currently no value.
middle_name = None

name = "Nantha"
age = 33
salary = 8500.50
is_developer = True

# Python gives you type().
print(type(name))
print(type(age))
print(type(salary))
print(type(is_developer))



# Python is dynamically typed
# string name = "Nantha"
# int age = 33
value = 10

print(type(value))

value = "hello"

print(type(value))


# variable cannot start with a number
# - is interpreted as subtraction
# 1name = "Nantha"
# first-name = "Nantha"


# Use snake_case:
first_name = "Nantha"
last_name = "Kumar"
monthly_salary = 8500
is_logged_in = True

# Avoid:
FirstName = "Nantha"
MonthlySalary = 8500
print(FirstName)


# Variables can be calculated
price = 100
quantity = 3

total = price * quantity

print(total)


price = 100
quantity = 3
tax = 30

subtotal = price * quantity
final_price = subtotal + tax

print(subtotal)
print(final_price)


# Variables can be changed
age = 32

print(age)

age = 33

print(age)

# Multiple assignment
name, age, city = "Nantha", 33, "Kuala Lumpur"

print(name)
print(age)
print(city)

# You can also assign the same value:
x = y = z = 100

print(x)
print(y)
print(z)

# Variables and strings

# Don't do this unnecessarily:
name = "Nantha"

print("My name is " + name)

# Python's f-strings are much cleaner:
name = "Nantha"    
age = 33

print(f"My name is {name} and I am {age} years old.")

# Variables + user input
name = input("Enter your name: ")

print(f"Hello, {name}!")


# input() always returns a string.

age = input("Enter your age: ")

print(type(age))


# Converting variables

age = int(input("Enter your age: "))

print(age)
print(type(age))
price = float(input("Enter price: "))
print(type(age))

# You can convert between common types:
age = "33"

age_number = int(age)

print(age_number + 1)


monthly_salary = 8500
months = 12

# Let's build a tiny salary calculator.
annual_salary = monthly_salary * months

print(f"Monthly salary: {monthly_salary}")
print(f"Annual salary: {annual_salary}")

# interactive
monthly_salary = float(input("Enter monthly salary: "))

annual_salary = monthly_salary * 12

print(f"Annual salary: {annual_salary}")


x = 10
y = x
print(x)

x = 10
y = x

x = 20

print(x)
print(y)

x = 10

print(x)
print(id(x))

x = 10
y = x

print(id(x))
print(id(y))