class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable


emp1 = Employee("Arun")
emp2 = Employee("Priya")

print(emp1.name)
print(emp2.name)

print(emp1.company)
print(emp2.company)