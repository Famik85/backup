# Завдання 1
# Реалізуйте клас «Людина». Необхідно зберігати в полях класу:
# ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до
# окремих полів за допомогою методи класу.

# class Human:
#     name = "Ivanov.I.I"
#     birthday = "15.11.1990"
#     telephone = "+38 099 345 45 67"
#     city = "Kyiv"
#     country = "Ukraine"
#     address = "top secret"
#
#     def __init__(self, name, birthday, telephone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.telephone = telephone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def __str__(self):
#         return f"Name : {self.name}\nBirthday : {self.birthday}\nTelephone: {self.telephone}\nCountry: {self.country}\nCity: {self.city}\nAddress: {self.address} "
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, new_birthday):
#         self.birthday = new_birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# warrior = Human("Warrior", "01.01.2000", "+380991234567", "Ukraine", "Kyiv", "incognito")
# print(warrior)
#
# warrior.set_name("God of war")
# print(warrior.get_name())
# warrior.set_birthday("At the beginning of time)")
# print(warrior.get_birthday())

# Завдання 2
# Створіть клас "Місто". Необхідно зберігати в полях класу: назва міста, назва регіону, назва країни,
# кількість жителів у місті, поштовий індекс міста, телефонний код міста. Реалізуйте методи класу для
# введення даних, виведення даних, реалізуйте доступ до окремих полів через методи класу.

# class City:
#     city_name = "Kyiv"
#     region_name = "Kyivska"
#     country_name = "Ukraine"
#     quntity_people = "2 679 653"
#     postcode = "01xxx->06xxx"
#     area_code = "+38 044"
#
#     def __init__(self, city_name, region_name, country_name, quntity_people, postcode, area_code):
#         self.city_name = city_name
#         self.region_name = region_name
#         self.country_name = country_name
#         self.quntity_people = quntity_people
#         self.postcode = postcode
#         self.area_code = area_code
#
#     def __str__(self):
#         return f"Name of city : {self.city_name}\nRegion name : {self.region_name}\nCountry: {self.country_name}\nQuantity of people: {self.quntity_people}\nPostcode: {self.postcode}\nArea code: {self.area_code} "
#
#     def set_city_name(self, new_city_name):
#         self.city_name = new_city_name
#
#     def get_city_name(self):
#         return self.city_name
#
#     def set_country_name(self, new_country_name):
#         self.country_name = new_country_name
#
#     def get_country_name(self):
#         return self.country_name
#
#
# lviv = City("Lviv", "Lvivska", "Ukraine", "735 000", "79000", "+38 032")
# print(lviv)
#
# lviv.set_city_name("New_Lviv")
# print(lviv.get_city_name())
# lviv.set_country_name("Poland")
# print(lviv.get_country_name())


# Завдання 3
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назва столиці, назва міст країни. Реалізуйте методи
# класу для введення даних, виведення даних, реалізуйте доступ до окремих полів через методи класу.

# class Country:
#     country_name = "Ukraine"
#     continent_name = "Europa"
#     population = "~ 30 m"
#     country_code = "+380"
#     capital_name = "Kyiv"
#     name_of_cities = "Lviv, Dnepr, Mariupol"
#
#     def __init__(self, country_name, continent_name, population, capital_name, name_of_cities, country_code):
#         self.country_name = country_name
#         self.continent_name = continent_name
#         self.population = population
#         self.capital_name = capital_name
#         self.name_of_cities = name_of_cities
#         self.country_code = country_code
#
#     def __str__(self):
#         return f"Name of country : {self.country_name}\nContinent name : {self.continent_name}\nPopulation : {self.population}\nCapital is : {self.capital_name}\nName of cities: {self.name_of_cities}\nCountry code: {self.country_code} "
#
#     def set_country_name(self, new_country_name):
#         self.country_name = new_country_name
#
#     def get_country_name(self):
#         return self.country_name
#
#     def set_capital_name(self, new_capital_name):
#         self.capital_name = new_capital_name
#
#     def get_capital_name(self):
#         return self.capital_name
#
# poland = Country("Poland", "Europa", "~ 38 m", "Warsaw", "Lodz, Gdansk, Poznan", "+48")
# print(poland)
#
# poland.set_country_name("France")
# print(poland.get_country_name())
# poland.set_capital_name("Paris")
# print(poland.get_capital_name())

# Завдання 4
# Створіть клас «Дроб». Необхідно зберігати у полях класу: чисельник та знаменник.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до
# окремим полям через методи класу. Також створіть методи класу для виконання арифметичних
# операцій(додавання, віднімання, множення, розподіл, і т.д.).

# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.validate_fraction()
#
#     def set_numerator(self, numerator):
#         self.numerator = numerator
#         self.validate_fraction()
#
#     def set_denominator(self, denominator):
#         self.denominator = denominator
#         self.validate_fraction()
#
#     def get_numerator(self):
#         return self.numerator
#
#     def get_denominator(self):
#         return self.denominator
#
#     def display(self):
#         print(f"{self.numerator}/{self.denominator}")
#
#     def validate_fraction(self):
#         if self.denominator == 0:
#             raise ValueError("Can't be 0.")
#
#     def add(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.get_denominator() + \
#                         other_fraction.get_numerator() * self.denominator
#         new_denominator = self.denominator * other_fraction.get_denominator()
#         return Fraction(new_numerator, new_denominator)
#
#     def subtract(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.get_denominator() - \
#                         other_fraction.get_numerator() * self.denominator
#         new_denominator = self.denominator * other_fraction.get_denominator()
#         return Fraction(new_numerator, new_denominator)
#
#     def multiply(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.get_numerator()
#         new_denominator = self.denominator * other_fraction.get_denominator()
#         return Fraction(new_numerator, new_denominator)
#
#     def divide(self, other_fraction):
#         if other_fraction.get_numerator() != 0:
#             new_numerator = self.numerator * other_fraction.get_denominator()
#             new_denominator = self.denominator * other_fraction.get_numerator()
#             return Fraction(new_numerator, new_denominator)
#         else:
#             raise ValueError("Can't be 0.")
#
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
#
# fraction1.display()
# fraction2.display()
#
# result_sum = fraction1.add(fraction2)
# result_sum.display()
#
# result_diff = fraction1.subtract(fraction2)
# result_diff.display()
#
# result_multiply = fraction1.multiply(fraction2)
# result_multiply.display()
#
# result_divide = fraction1.divide(fraction2)
# result_divide.display()

