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