# function
var1 =20
def HBTY(name,age):
    print("Hello, World!")
    print("HBTY " + name)
    print("Age: " + str(age))

HBTY("John", 30)

class CAR:
    # attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # methods
    def start_engine(self):
        print("Engine started!")

    def stop_engine(self):
        print("Engine stopped!")

    # parameter in methods
    def display_info(self,color):
        print(f"Car Info: {self.brand} {self.model} ({self.year}), Color: {color}")

maruti = CAR("Maruti", "Swift", 2020)
maruti.start_engine()
maruti.display_info("Red")