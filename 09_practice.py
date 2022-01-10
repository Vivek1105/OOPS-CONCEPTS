#1st question

# class Coders:
#     company = "adobe"

#     def __init__(self, name, id, dep):
#         self.name = name
#         self.id = id
#         self.dep = dep

#     def getinfo(self):
#         print(f"company name is  {self.company} coder name is {self.name} coder id is  {self.id} and the product is  {self.dep}")

# vivek = Coders("vivek", 123, "apppdev")
# vivek.getinfo()
        

  


#2nd question
# class Calculator:
#     def __init__(self,num):
#         self.number = num

#     def square(self):
#         print(f"the valu of {self.number} suare is {self.number **2}")

#     def squareroot(self):
#         print(f"the valu of {self.number} suareroot is {self.number **0.5}")

#     def cube(self):
#         print(f"the valu of {self.number} cube is {self.number **3}")


# a = Calculator(9)
# a.square()
# a.squareroot()
# a.cube()



# 3rd question 
# class Test:
#     a = "vivek"

# obj = Test()
# obj.a = "singh"

# print(Test.a)
# print(obj.a)
        


# 4th question 
class train:
    def __init__(self, name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"train name is {self.name} avilable seats are {self.seats}")

    def fareInfo(self):
        print(f"tickests price is {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"your ticket bokked{self.seats}")
            self.seats = self.seats-1
        else:
            print("tickets not avilable")


express = train("garib rath", 1000, 50)
express.getStatus()
express.bookTicket()
express.fareInfo()


        
        
        
