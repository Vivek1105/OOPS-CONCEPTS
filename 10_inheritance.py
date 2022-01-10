class Employee:
    company = "amazon"


    def ShowDetails(self):
        print("this is employee")

class  Coder(Employee):
    language = "python"
    company = "oracal"


    # def getlanguage(self):
    #     print(f"the language is {self.language}")

    def ShowDetails(self):
        print("this is coder")


e = Employee()
e.ShowDetails()
c = Coder()
c.ShowDetails()
print(c.company)
