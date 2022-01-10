class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

viveksApplication = RailwayForm()
viveksApplication.name = "vivek"
viveksApplication.train = "Rajdhani Express"
viveksApplication.printData()