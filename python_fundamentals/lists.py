fruits = ["apple", "banana", "orange"]

print(fruits)

data = ["Nantha", 33, True, 10.5]

print(data)


# Access List Items
fruits = ["apple", "banana", "orange", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative indexing
print("------negative indexing-----")
print(fruits[-1])  # mango
print(fruits[-2])  # orange

print("------Change List Items-----")
fruits = ["apple", "banana", "orange"]

fruits[1] = "mango"

print(fruits)

print("------append-----")
fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)

print("------insert-----")
fruits = ["apple", "orange"]

fruits.insert(1, "banana")
fruits.insert(2, "grapes")
print(fruits)

print("------extend-----")
fruits = ["apple", "banana"]

fruits.extend(["orange", "mango"])
fruits.append(["grapes", "orange"])

print(fruits)



