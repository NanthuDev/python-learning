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
elif age >= 18 and not has_active:
    print("Valid but inactive user")
else:
    print("Invalid user")

print("Multiple conditions with or")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Working day")


print("---- not reverses a Boolean value ---- ")
is_raining = False

if not is_raining:
    print("You can go outside")

print("---- Combining conditions ---- ")

age = 25
has_ticket = True
is_banned = False

if age >= 18 and has_ticket and not is_banned:
    print("Entry allowed")
else:
    print("Entry denied")
print("---- Combining conditions 2 ---- ")
today ="monday"
got_taxi = False
can_go = False

if today == "monday" and got_taxi and not can_go:
    print("can go outside")
else:    
    print("cant go")

print("---- Nested conditions ---- ")
age = 12
has_active = False

if age >= 18:
    if has_active:
        print("Active user")
    else:
        print("Inactive user")
else:
    print("Invalid user")

# However, don't overuse nested conditions. Often you can simplify them:
if age >= 18 and has_active:
    print("Entry allowed")
else:
    print("Entry denied")

print("---- Conditions with strings ---- ")
username = "admin"

if username == "admin":
    print("Welcome Admin")
else:
    print("Welcome User")

email = "user@gmail.com"

if "@" in email:
    print("Looks like an email")
else:
    print("Invalid email")

print("---- Conditions with lists ---- ")
languages = ["Python", "JavaScript", "Java"]

if "Python" in languages:
    print("Python is available")
if "C++" not in languages:
    print("C++ is not available")

print("---- Truthy and Falsy values ---- ")
username = "ss"

if username:
    print("Username exists")
else:
    print("Username is empty")
# Common falsy values include:
# False
# None
# 0
# ""
# []
# {}

listss = {}

if listss:
    print("yeah")
else:
    print("not okay")