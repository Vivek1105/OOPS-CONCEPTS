class Employee:
    cpmpany = "google"
    def getsalary(self):
        print(f"salary of this employee who worked in {self.cpmpany} is {self.salary}")

    @staticmethod
    def time():
        print("the city which you live bihar")
   
    @staticmethod
    def greet():
        print("hey gud mrng ")


vivek = Employee()
vivek.salary = 10000
vivek.getsalary()         #Employee.getsalary(vivek)
vivek.time()
vivek.greet()