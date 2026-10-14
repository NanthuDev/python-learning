class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")


student1 = Student("Arun", 20)
student2 = Student("Priya", 22)    

student1.introduce()
student2.introduce()  