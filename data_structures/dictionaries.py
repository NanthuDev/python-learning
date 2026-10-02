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