print("tuple can contain different data types:")
person = ("Nantha", 33, "Malaysia")

print(person)


numbers = (10, 20, 30)

# numbers[0] = 100

# List   → [] → can change
# Tuple  → () → cannot change


person = ("Nantha", 33, "Malaysia")

print(person[0])
print(person[1])
print(person[2])

person = ("Nantha", 33, "Malaysia")

print(person[-1])
print(person[-2])


numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

number = (10)
print(type(number))
number = (10,)

print(type(number))

person = "Nantha", 33, "Malaysia"

print(person)
print(type(person))

person = ("Nantha", 33, "Malaysia")

name,  country,age = person

print(name)
print(age)
print(country)

a = 10
b = 20

a, b = b, a

print(a)
print(b)

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))

numbers = (10, 20, 30, 40)

print(numbers.index(30))


languages = ("Python", "JavaScript", "Java", "Go")

print("Python" in languages)
print("C++" in languages)


languages = ("Python", "JavaScript", "Java")

for language in languages:
    print(language)