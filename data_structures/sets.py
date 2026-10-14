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


required_skills = {"Python", "SQL"}
developer_skills = {"Python", "SQL", "Git", "Docker"}

print(required_skills.issubset(developer_skills))
print(developer_skills.issuperset(required_skills))


print(required_skills <= developer_skills)  # True
print(developer_skills >= required_skills)  # True


user_ids = [101, 102, 101, 103, 102, 104, 101]

unique_user_ids = set(user_ids)

print(unique_user_ids)
print(len(unique_user_ids))


user_ids = [101, 102, 101, 103, 102, 104]

unique_user_ids = list(dict.fromkeys(user_ids))

print(unique_user_ids)


numbers = [1, 2, 2, 3, 4, 4, 5, 6]

even_numbers = {number for number in numbers if number % 2 == 0}

print(even_numbers)


user_permissions = {"read", "write", "update"}

required_permissions = {"read", "write"}

if required_permissions.issubset(user_permissions):
    print("Access granted")
else:
    print("Access denied")


user_ids = [101, 102, 101, 103, 102, 104]

print(dict.fromkeys(user_ids))

unique_user_ids = list(dict.fromkeys(user_ids))

print(unique_user_ids)
