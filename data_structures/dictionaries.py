user = {
    "name": "Nantha",
    "age": 33,
    "role": "Developer",
    "is_active": True
}

print(user)


user = {
    "name": "Nantha",
    "age": 33,
    "role": "Developer"
}

print(user["name"])
print(user["age"])

# print(user["email"])

print(user.get("email"))
print(user.get("email", "Not provided"))


user = {
    "name": "Nantha",
    "role": "Developer"
}

# Add a new key-value pair
user["email"] = "nantha@example.com"

# Update an existing value
user["role"] = "Senior Developer"

print(user)


user = {
    "name": "Nantha",
    "age": 33,
    "role": "Developer"
}

# Remove a specific key
del user["age"]

# Remove a key and return its value
role = user.pop("role")

print(user)
print(role)

user.clear()
print(user)  # {}

print(user.pop("email", None))  # {}


user = {
    "name": "Nantha",
    "age": 33,
    "role": "Developer"
}

print(user.keys())
print(user.values())
print(user.items())


user = {
    "name": "Nantha",
    "role": "Developer",
    "city": "Kuala Lumpur"
}

for key in user:
    print(key)

for value in user.values():
    print(value)


for key, value in user.items():
    print(f"{key}: {value}")


    users = {
    101: {
        "name": "Arun",
        "role": "Developer"
    },
    102: {
        "name": "Priya",
        "role": "Tester"
    }
}

print(users[101]["name"])
print(users[102]["role"])


squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)

print(squares[4])

# {key_expression: value_expression for item in iterable}