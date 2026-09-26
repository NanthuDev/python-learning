def greet(name):
    print("Hello", name)

greet("John")
greet("David")
greet("Sarah")

#Basic
# def function_name(parameters):
    # code
# calling it
# function_name(arguments)


def say_hello():
    print("Hello!")


say_hello()


# Multiple parameters
def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old")


introduce("John", 25)

# return

def add(a, b):
    return a + b


result = add(10, 20)

print(result)

# Function with a condition
def check_age(age):

    if age >= 18:
        return "Adult"
    else:
        return "Minor"


result = check_age(25)

print(result)


# Default parameters

def greet(name="Guest"):
    print("Hello", name)


greet()
greet("John")


# Keyword arguments

def introduce(name, age):
    print(name, age)


introduce(age=30, name="John")


# Returning multiple values
def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print(result)

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)

# Function calling another function
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(a, b):

    result = add(a, b)

    return multiply(result, 2)


print(calculate(10, 20))

# Type hints
def add(a: int, b: int) -> int:
    return a + b

# meaning:
# a       → int
# b       → int
# return  → int