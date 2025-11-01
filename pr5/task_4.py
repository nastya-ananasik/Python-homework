class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Двигун {self.make} {self.model} ({self.fuel_type}) запущено.")

    def display_info(self):
        print(f"Автомобіль: {self.make} {self.model} ({self.year}), тип палива: {self.fuel_type}.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def wheelie(self):
        print(f"{self.make} {self.model} робить 'віллі'!")

    def display_info(self):
        print(f"Мотоцикл: {self.make} {self.model} ({self.year}), тип: {self.bike_type}.")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print(f"Велосипед {self.make} {self.model} дзвонить: Дзінь-дзінь!")

    def display_info(self):
        print(f"Велосипед: {self.make} {self.model} ({self.year}), кількість передач: {self.num_gears}.")


my_car = Car("Toyota", "Camry", 2022, "Бензин")
my_moto = Motorcycle("Harley-Davidson", "Sportster", 2019, "Круізер")
my_bike = Bicycle("Trek", "Marlin 5", 2023, 21)

vehicles_list = [my_car, my_moto, my_bike]

generic_vehicle = Vehicle("Generic", "Transporter", 2000)
vehicles_list.append(generic_vehicle)

for vehicle in vehicles_list:
    vehicle.display_info()
