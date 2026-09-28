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

print("------remove-----")

fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)

print("------pop-----")
fruits = ["apple", "banana", "orange"]

removed = fruits.pop(2)

fruits.pop()
print(removed)
print(fruits)

print("------clear-----")
fruits = ["apple", "banana", "orange"]

fruits.clear()

print(fruits)

print("------len-----")
fruits = ["apple", "banana", "orange"]

print(len(fruits))


print("------index-----")

fruits = ["apple", "banana", "orange"]

position = fruits.index("apple")

print(position)

print("------count-----")
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

print("------sort-----")
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
print("------sort desc----")

numbers.sort(reverse=True)

fruits = ["apple", "banana", "orange"]

fruits.reverse()

print(fruits)


print("------Check if an Item Exists----")

fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
print("grape" in fruits)

if "banana" in fruits:
    print("Banana is available")









