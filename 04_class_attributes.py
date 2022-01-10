class Employee:
    company = "amazone"

vivek = Employee()
shruti = Employee()
print(vivek.company)
print(shruti.company)


Employee.company = "google"
print(vivek.company)
print(shruti.company)
