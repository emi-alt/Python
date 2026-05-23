class Person:
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    def display(self):
        print(self.name)
        print(self.idnum)

class Employee(Person):
    def __init__(self, name, idnum, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnum)

a = Employee("Paul", 879045, 10000, "Intern")
a.display()
