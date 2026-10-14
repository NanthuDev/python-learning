for i in range(5):
    print("Hello")


for i in range(5):
    print(i)

for i in range(3):
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print("even")

ages = [15, 22, 17, 30, 14, 25]
for age in ages:
    if age >= 18:
        print(age)

letter = "print"

for let in letter:
    print(let)


count = 1

while count <= 5:
    print(count)
    count = count + 1

count = 3
while count <= 5:
    print(count)
    count = count + 1

print("_____")
for i in range(1, 10):
    if i == 5:
        break

    print(i)

print("__%%%%___")


for i in range(1, 6):
    if i == 3:
        continue

    print(i)

print("Nested Loops")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
 