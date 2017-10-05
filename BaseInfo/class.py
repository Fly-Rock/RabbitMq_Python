#coding=UTF-8
class Car():

    def __init__(self,make,model,year):
        self.make  = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(self.make + self.model)

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it ")


    #通过方法修改属性
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")


#继承
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + " kwh battery")

#user 继承
elec_class = ElectricCar("testla","model s",2015)
elec_class.describe_battery()

#use car class
my_new_car = Car("audi","A4",2017)
my_new_car.get_descriptive_name()
my_new_car.read_odometer()
my_new_car.odometer_reading = 10
my_new_car.read_odometer()
#通过方法修改属性
my_new_car.update_odometer(2)




