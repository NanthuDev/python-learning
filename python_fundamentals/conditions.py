# if condition:
#     # code runs when condition is True

age = 20

if age >= 18:
    print("You are an adult")


temperature = 30
if temperature >= 20:
    print("cit is hotter")


print("conditions")

age = 25

print(age == 25)
print(age > 18)
print(age < 18)
print(age != 30)


age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


print("practice conditions")

password = "temdp"

if password == 'temp':
    print("its correct")
else:
    print("not correct")



print("If...Elif")

marks = 92

if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 30:
    print("D Grade")
else:
    print("Fail")

print("Multiple conditions with and")

age = 25
has_active = False

if age >= 18 and has_active:
    print("Valid user")
elif age >= 18 and has_active == False:
    print("Valid but inactive user")
else:
    print("Invalid user")

print("Multiple conditions with or")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Working day")