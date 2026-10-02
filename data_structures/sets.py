numbers = {10, 20, 30, 20, 10}

print(numbers)


# Set of integers
numbers = {1, 2, 3, 4, 5}

# Set of strings
languages = {"Python", "JavaScript", "Java"}

# Set with mixed data types
data = {10, "Python", True}

print(numbers)
print(languages)
print(data)

empty_set = set()
empty_dictionary = {}

print(type(empty_set))
print(type(empty_dictionary))

languages = {"Python", "JavaScript"}

languages.add("Java")
languages.add("Python")

print(languages)

languages = {"Python", "JavaScript"}

languages.update(["Java", "Go", "C++"])

print(languages)


numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)

numbers.discard(100)
print(numbers)

skills = {"Python", "Node.js", "SQL"}

print("Python" in skills)
print("Java" in skills)


skills = {"Python", "Node.js", "SQL"}

for skill in skills:
    print(skill)

numbers = {50, 10, 40, 20, 30}

for number in sorted(numbers):
    print(number)



developer_a = {"Python", "SQL", "Git"}
developer_b = {"Python", "JavaScript", "Git"}

# Union
print(developer_a | developer_b)

# Intersection
print(developer_a & developer_b)

# Difference
print(developer_a - developer_b)

# Symmetric difference
print(developer_a ^ developer_b)