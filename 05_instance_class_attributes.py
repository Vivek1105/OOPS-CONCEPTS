class Employee:
    company = "amazone"
    salary = 100
    address ="jngfbvd" 

vivek = Employee()
shruti = Employee()

#creating instance attributes "salary" for both the object 
vivek.salary = 500
shruti.salary = 1000


vivek.salary = 50
print(vivek.salary)
print(shruti.salary)
print(vivek.company)
print(shruti.company)

#below line throws an error as address is not present in instance/class
print(vivek.address)

