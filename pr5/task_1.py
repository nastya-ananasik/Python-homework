class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} ({self.species}): {self.sound}!")

dog = Animal("Бублик", "Собака", 3, "Гав-гав")
cat = Animal("Тиша", "Кіт", 2, "Няв")

dog.make_sound()
cat.make_sound()
