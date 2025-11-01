class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Двигун {self.make} {self.model} ({self.fuel_type}) запущено.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def wheelie(self):
        print(f"{self.make} {self.model} робить 'віллі'!")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print(f"Велосипед {self.make} {self.model} дзвонить: Дзінь-дзінь!")

my_car = Car("Toyota", "Camry", 2022, "Бензин")
my_moto = Motorcycle("Harley-Davidson", "Sportster", 2019, "Круізер")
my_bike = Bicycle("Trek", "Marlin 5", 2023, 21)

print(f"Авто: {my_car.make} {my_car.model}, Паливо: {my_car.fuel_type}")
my_car.start_engine()

print(f"\nМото: {my_moto.make} {my_moto.model}, Тип: {my_moto.bike_type}")
my_moto.wheelie()

print(f"\nВело: {my_bike.make} {my_bike.model}, Передачі: {my_bike.num_gears}")
my_bike.ring_bell()
