# Ryder Meehan
# m03_lab.py
# This program utilizes classes and the super() class function
# to ask the user for vehicle information and store each attribute
# into the Automobile class and then output the vehicle information
# back to the user in an organized format

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

type = input("Enter type of vehicle: ")

year = input("Year: ")

make = input("Make: ")

model = input("Model: ")

doors = input("Number of doors: ")

roof = input("Roof type: ")

whip = Automobile(type, year, make, model, doors, roof)

print("\nVehicle Info\n_____________\n")
print("Vehicle Type:", whip.type)
print("Year:", whip.year)
print("Make:", whip.make)
print("Model:", whip.model)
print("Doors:", whip.doors)
print("Roof Type:", whip.roof)

input("Press ENTER to exit") #put this here to stop the program from immediately closing once output was complete
