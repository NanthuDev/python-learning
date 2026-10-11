class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing Python code")

class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting")


dev = Developer("Arun", 6000)
manager = Manager("Priya", 8000)

dev.show_details()
dev.write_code()

manager.show_details()
manager.conduct_meeting()