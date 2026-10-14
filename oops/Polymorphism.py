class Developer:
    def work(self):
        print("Developer writes code")

class Tester:
    def work(self):
        print("Tester tests the application")


class DevOpsEngineer:
    def work(self):
        print("DevOps engineer manages deployment")

team = [
    Developer(),
    Tester(),
    DevOpsEngineer()
]

for employee in team:
    employee.work()