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
