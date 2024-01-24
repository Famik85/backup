#https://python-scripts.com/object-oriented-programming-in-python

#Процедурный (функцуональный)

# def hello(name):
#     result = f"Hello my name is {name}. "
#     return result
#
# print(hello("Andrii"))
# print(hello("Sten"))
# print(hello("Ben"))

#ООП

# class Borsch:
#     value = 2  # Атрибут\аргумент\параметр\поле (переменная класса)
#     beet = True # Могут быть любого типа
#     meat = "pork"
#
#     def boiled(self, temperature):   # Метод объекта класса(функция объекта класса)
#         if temperature > 100:
#             return "You boiled borsch"
#         else:
#             return "You need more"
#
# odesa_borsch = Borsch()
#
# print(odesa_borsch.value)
# print(odesa_borsch.boiled(101))
# print(odesa_borsch.boiled(50))

class Borsch:
    value = 2  # Атрибут\аргумент\параметр\поле (переменная класса)
    beet = True # Могут быть любого типа
    meat = "pork"

    def boiled(self, temperature):   # Метод объекта класса(функция объекта класса)
        if temperature > 100:
            return "You boiled borsch"
        else:
            return "You need more"

odesa_borsch = Borsch()

# print(odesa_borsch.value)
# print(odesa_borsch.meat)
# odesa_borsch.meat = "veal"
# print(odesa_borsch.meat)

# mariupol_borsch = Borsch()
# mariupol_borsch.meat = "chicken"
# mariupol_borsch.cabbage = True
# mariupol_borsch.sour_cream = True
# print(mariupol_borsch.meat)
# print(mariupol_borsch.cabbage)
# print(mariupol_borsch.sour_cream)

# Наследование
# Полиморфизм
# Инкапсуляция

# Абстракция


# Наследование
class Human:
    age = 20
    name = "Sten"
    profession = "empty"
    def eat(self):
        return "You eat"
class Builder(Human):
    profession = "builder"
    def builder(self):
        return

class Sailor(Human):
    age = 28
    profession = "Sailor"
    def sea(self):
        return "I love the sea"

class Pilot(Human):
    age = 20
    profession = "Pilot"
    def sky(self):
        return "I'm flying in the sky"

class SeaBuilder(Builder, Sailor):
    pass

seal = SeaBuilder()
print(seal.age)
print(seal.profession)

# Полиморфизм

class MeatShreder:
    def shred(self,meat):
        if meat == "pork":
            return f"Shreded {meat}"
        elif meat == "bark":
            return f"Sawdust {meat}"

saw = MeatShreder()
print(saw.shred("pork"))
print(saw.shred("bark"))

# Инкапсуляция

class Car:
    def __init__(self):
        self.name = "corolla"   #public
        self._model = 1999      #_protected
        self.__make = "toyota"  #__privat

t = Car()
print(t.name)
t.name = "hilux"
print(t.name)
print(t._model)
t._model = "123"
print(t._model)