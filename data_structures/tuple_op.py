# 1. Create a tuple

person = ("Nantha", 33, "Malaysia")

print(person)


# 2. Access elements

print(person[0])
print(person[1])
print(person[2])


# 3. Negative indexing

print(person[-1])


# 4. Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])


# 5. Count

values = (10, 20, 10, 30, 10)

print(values.count(10))


# 6. Index

print(values.index(30))


# 7. Membership

languages = ("Python", "JavaScript", "Java")

print("Python" in languages)


# 8. Loop

for language in languages:
    print(language)


# 9. Unpacking

name, age, country = person

print(name)
print(age)
print(country)


# 10. Swapping

a = 10
b = 20

a, b = b, a

print(a)
print(b)