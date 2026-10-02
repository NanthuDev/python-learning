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