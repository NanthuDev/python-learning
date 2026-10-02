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