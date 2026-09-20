# integer

a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a // b)  # floor division
print(a % b)   # remainder
print(a ** b)  # power


print(type(a))

# float
height = 5.9
price = 99.99
temperature = 32.5

print(type(height))
print(type(price))
print(type(temperature))
price = 100.50
quantity = 3

total = price * quantity

print(total)
print(type(total))


# String
print("------String-----")
name = "John"
city = 'Kuala Lumpur'
job = "Software Engineer"

print(name)
print(city)
print(job)

first_name = "John"
last_name = "Doe"
print(f"full name:{first_name} {last_name}")

full_name = first_name + " " + last_name

print(full_name)
name = "joHn"

print(name.upper())
print(name.lower())
print(name.capitalize())
name = "Python"

print(len(name))
print(name[0])
print(name[1])
print(name[2])

# bool
print("------Bool-----")

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)
print(type(is_logged_in))

age = 20

is_adult = age >= 18

print(is_adult)

password_correct = True

if password_correct:
    print("Login successful")


# list — Collection of Values

fruits = ["apple", "banana", "orange"]

print(fruits)

print(fruits[0])
print(fruits[1])


# Lists can contain different types
data = ["John", 33, 5000.50, True]

print(data)
ages = [20, 25, 30, 35]

fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)

# tuple — Fixed Collection

coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
coordinates = (10, 20)

# coordinates[0] = 100

# list  → can change
# tuple → cannot change

# set — Unique Values,unique values,intersection, union, difference

numbers = {10, 20, 30}

print(numbers)

numbers = {10, 20, 20, 30, 30}

print(numbers)

skills = {"Python", "JavaScript", "Python", "SQL"}

print(skills)


# dict — Key-Value Data
user = {
    "name": "John",
    "age": 33,
    "job": "Software Engineer"
}

print(user["name"])
print(user["age"])
print(user["job"])

user["city"] = "Kuala Lumpur"

print(user)

user["age"] = 34

print(user)

# None — No Value
result = None

print(result)
print(type(result))

user = None

if user is None:
    print("User not found")

# there is no value.