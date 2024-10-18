# class Car:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         print(f"The {self.make} {self.model}\'s is starting")
#
#     def drive(self, distance):
#         print(f"The {self.make} {self.model}\'s is driving {distance} kilometers")
#
#     def stop_engine(self):
#         print(f"The {self.make} {self.model}\'s engine is stopping")
#
#
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Mercedes", "S500", 2021)
# print(car1.make)
# print(car2.year)
# car1.start_engine()
# car2.start_engine()
# car2.drive(200)
# car2.start_engine()

# 2/ do not use init method
# class Car:
# def set_model(self, model):
#     self.model = model
#
# def set_color(self, color):
#     self.color = color
#
# def display_info(self):
#     print(f"Model: {self.model},Color: {self.color}")


# car = Car()
# car.set_model("Toyota Corolla")
# car.set_color("Blue")
# car.display_info()

# 3/ create object
# class Car:
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#     def display_info(self):
#         print(f"Model: {self.model},Color: {self.color}")
#
#
# car = Car("Toyota Corolla", "Blue")
# car.display_info()
