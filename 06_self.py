class Employee:
    cpmpany = "google"
    def getsalary(self):
        print(f"salary of this employee who worked in {self.cpmpany} is {self.salary}")


vivek = Employee()
vivek.salary = 10000
vivek.getsalary()         #Employee.getsalary(vivek)