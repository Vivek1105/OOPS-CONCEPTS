class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath() 

e = Employee()
e.takeBreath() 

pr = Programmer()
pr.takeBreath() 
