# "** https://python-scripts.com/object-oriented-programming-in-python"
#
# #Процедурний (Функціональний)
#
# def hello(name):
#     result = f"Hello my name is {name}."
#     return result
#
# print(hello('Andrii'))
# print(hello('Sten'))
# print(hello('Ben'))
#
# #ООП
# a = int(5) # int є вбудованим классом
############
# class Borsch: # креслення, рецепт, інструкція
#     value = 2 # атрибут класу, аргумент класу, параметр класу, поля класу(змінна класу)
#     beet = True # можуть юути будь-якого типу
#     meat = 'pork'
#
#     def boiled(self, temperature): # метод обʼекту класа (функція обʼекту класу)
#         if temperature > 100:
#             return 'You boiled borsch'
#         else:
#             return 'You need more'
#
# odesa_borsch = Borsch() # те що ви зробили за цим кресленням, рецептом, інструкцією

# print(odesa_borsch.value)
# print(odesa_borsch.boiled(101))
# print(odesa_borsch.boiled(50))

# a = int()
# hello()

class Borsch: # креслення, рецепт, інструкція
    value = 2 # атрибут класу, аргумент класу, параметр класу, поля класу(змінна класу)
    beet = True # можуть юути будь-якого типу
    meat = 'pork'

    def boiled(self, temperature): # метод обʼекту класа (функція обʼекту класу)
        if temperature > 100:
            return 'You boiled borsch'
        else:
            return 'You need more'

odesa_borsch = Borsch()
print(odesa_borsch.value)
print(odesa_borsch.meat)
odesa_borsch.meat = 'veal'# телятина
print(odesa_borsch.meat)

lviv_borsch = Borsch()
lviv_borsch.meat = 'chicken'
print(lviv_borsch.meat)

herson_borsch = Borsch()
herson_borsch.beet = False
herson_borsch.tomato = True
print(herson_borsch.tomato)

# Наслідування
# Поліморфізм
# Інкапсуляція

# Абстракція


# Наслідування

class Human:
    age = 20
    name = 'Sten'
    profession = 'empty'
    def eat(self):
        return 'You eat'

class Buider(Human):
    profession = 'builder'
    def build(self):
        return 'You build house'
class Pilot(Human):
    profession = 'pilot'
    def fly(self):
        return 'You transport cargo by air'
class Sailor(Human):
    profession = 'sailor'
    def swim(self):
        return 'You transport cargo by water'

class SeaBuilder(Buider,Sailor):
    pass

seal = SeaBuilder()
print(seal.profession)
#Pilot, Sailor
# bender = Buider()
# print(bender.name)
# print(bender.profession)
# print(bender.build())


# Поліморфізм

class MeatShreder:
    def shred(self,meat):
        if meat == "pork":
            return f"Shreded {meat}"
        elif meat == "bark":
            return f"Sawdust {meat}"

saw = MeatShreder()
print(saw.shred('pork'))
print(saw.shred('bark'))

# Інкапсуляція

class Car:
    def __init__(self):
        self.name = "corolla"   #public
        self._model = 1999      #_protected
        self.__make = "toyota"  #__privat

t = Car()
print(t.name)
t.name = 'hilux'
print(t.name)
t._model = '123'
print(t._model)