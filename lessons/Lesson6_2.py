class Box:
    material = 'paper'
    _weight = 10
    __health = 100
    __id = 1

    def __init__(self, name):
        self.__id = Box.__id
        Box.__id = Box.__id + 1
        self.name = name

    def __str__(self):
        return f"Name : {self.name} ID : {self.__id}"

    def set_name(self,new_name):
        # new_name = input("Enter name : ")
        self.name = new_name

    def get_name(self):
        # print(self.name)
        return self.name

nowapost = Box('np')
meest = Box('meest')
nightexpress = Box('ne')

print(nowapost)
print(meest)
print(nightexpress)

nightexpress.set_name('Night')
print(nightexpress.get_name())
