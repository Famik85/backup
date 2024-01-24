# Завдання 1
# Створіть клас Human, який буде містити інформацію про людину.
# За допомогою механізму успадкування реалізуйте клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot (містить інформацію про льотчика).
# Кожен з класів повинен містити необхідні методи для роботи.

# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def show(self):
#         print(f"My name is {self.name}. I am {self.age} years old. I am a {self.gender}.")
#
#
# class Builder(Human):
#     def __init__(self, name, age, gender, construction_experience):
#         Human.__init__(self, name, age, gender)
#         self.construction_experience = construction_experience
#
#     def build(self):
#         print(f"{self.name} with {self.construction_experience} years of construction experience is building a house.")
#
#
# class Sailor(Human):
#     def __init__(self, name, age, gender, sailing_experience):
#         Human.__init__(self, name, age, gender)
#         self.sailing_experience = sailing_experience
#
#     def sail(self):
#         print(f"{self.name} with {self.sailing_experience} years of sailing experience, steers the ship.")
#
#
# class Pilot(Human):
#     def __init__(self, name, age, gender, flying_experience):
#         Human.__init__(self, name, age, gender)
#         self.flying_experience = flying_experience
#
#     def fly(self):
#         print(f"{self.name} flies the plane with {self.flying_experience} years of flying experience.")
#
#
# builder_ivan = Builder("Ivan", 35, "man", 10)
# sailor_maria = Sailor("Maria", 28, "woman", 5)
# pilot_oleg = Pilot("Oleg", 40, "man", 15)
#
# builder_ivan.show()
# builder_ivan.build()
#
# sailor_maria.show()
# sailor_maria.sail()
#
# pilot_oleg.show()
# pilot_oleg.fly()

# Завдання 2
# Створіть клас Passport (паспорт), який буде містити паспортну інформацію про громадянина заданої
# країни. За допомогою механізму успадкування реалізуйте клас ForeignPassport (загр.паспорт),
# що є похідним від Passport. Нагадаємо, що закордонний паспорт містить, крім паспортних даних,
# також інформацію про візи та номер заграничного паспорта. Кожен з класів повинен містити необхідні
# методи.

# class Passport:
#     def __init__(self, full_name, date_of_birth, nationality, passport_number):
#         self.full_name = full_name
#         self.date_of_birth = date_of_birth
#         self.nationality = nationality
#         self.passport_number = passport_number
#
#     def display_info(self):
#         print(f"Passport info:\nFull name: {self.full_name}\nDate of Birth: {self.date_of_birth}\n"
#               f"Nationality: {self.nationality}\nPassport number: {self.passport_number}")
#
#
# class ForeignPassport(Passport):
#     def __init__(self, full_name, date_of_birth, nationality, passport_number, visa_info, foreign_passport_number):
#         Passport.__init__(self, full_name, date_of_birth, nationality, passport_number)
#         self.visa_info = visa_info
#         self.foreign_passport_number = foreign_passport_number
#
#     def display_info(self):
#         print(f"Foreign passport:\nForeign passport number: {self.foreign_passport_number}\n"
#               f"Visa info: {self.visa_info}")
#         Passport.display_info(self)
#
#
# passport = Passport("Ivanov Ivan Ivanovich", "01.01.1990", "Ukraine", "AB123456")
# passport.display_info()
#
# foreign_passport = ForeignPassport("Ivanov Ivan Ivanovich", "01.01.1990", "Ukraine", "AB123456",
#                                     "Visa to USA, Visa to Europe", "FP987654")
# foreign_passport.display_info()

# Завдання 3
# Створіть базовий клас "Тварина" і похідні класи "Тигр", "Крокодил", "Кенгуру".
# За допомогою конструктора встановіть ім'я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.

# class Animal:
#     def __init__(self, name, species, habitat):
#         self.name = name
#         self.species = species
#         self.habitat = habitat
#
#     def make_sound(self):
#         pass
#
#     def move(self):
#         pass
#
#     def display_info(self):
#         print(f"Name: {self.name}\nSpecies: {self.species}\nHabitat: {self.habitat}")
#
# class Tiger(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name, "Tiger", "Forest areas")
#
#     def make_sound(self):
#         print("Rrrr!")
#
#     def move(self):
#         print("Tiger walks on 4 legs.")
#
# class Crocodile(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name, "Crocodile", "Reservoirs")
#
#     def make_sound(self):
#         print("Grrr!")
#
#     def move(self):
#         print("Crocodile swims in the water.")
#
# class Kangaroo(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name, "Kangaroo", "Steppe territories")
#
#     def make_sound(self):
#         print("Rrrr!")
#
#     def move(self):
#         print("Kangaroo jumps on its hind legs.")
#
# tiger = Tiger("Sherkhan")
# tiger.display_info()
# tiger.make_sound()
# tiger.move()
#
# crocodile = Crocodile("Gena crocodile")
# crocodile.display_info()
# crocodile.make_sound()
# crocodile.move()
#
# kangaroo = Kangaroo("Kangaroo Jack")
# kangaroo.display_info()
# kangaroo.make_sound()
# kangaroo.move()