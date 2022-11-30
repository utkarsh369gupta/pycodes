class Employee:
    def __init__(self,na,sa,ro):
        self.name=na
        self.salary=sa
        self.role=ro
    def details(self):
        return f"Name of employee is {self.name} who is {self.role} with salary is {self.salary}."
utk=Employee("utkarsh",70000,"software engineer")
print(utk.details())
print(utk.name)


class Employee():
    no_of_leaves=8
emp1=Employee()
emp2=Employee()
emp1.name="harry"
emp1.no_of_leaves=4
print(emp1.__dict__)
print(Employee.__dict__)
Employee.no_of_leaves=5
print(Employee.__dict__)
print(emp2.no_of_leaves)


class Employee:
    def __init__(self,na,sa,ro):
        self.name=na
        self.salary=sa
        self.role=ro
    @classmethod
    def sal(cls,sa):
        cls.salary=sa
    def details(self):
        return f"Name of employee is {self.name} who is {self.role} with salary is {self.salary}."
utk=Employee("utkarsh",70000,"software engineer")
ang=Employee("angel",170000,"software manager")
print(utk.details())
utk.salary=30
utk.sal(40)
print(utk.details())
print(ang.details())
# print(Employee.__dict__)