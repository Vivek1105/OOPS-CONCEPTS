class Employee:
    cpmpany = "google"


    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self .subunit = subunit
        print("employee is created")

    def getdetails(self):
        print(f"employee name is {self.name}")
        print(f"employee salary is {self.salary}")
        print(f"employee subunit  is {self.subunit}")


vivek = Employee("vivek", 10010, "amazon")
vivek.getdetails()
#vivek = Employee()        this throws an error (missing 3 required positional arguments:)

        



    
