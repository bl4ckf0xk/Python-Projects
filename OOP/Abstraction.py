class Special:
    __hiddenValue = 10

    def add(self, incrment):
        self.__hiddenValue += incrment
        print(self.__hiddenValue)


Userdef = Special()
Userdef.add(1)
Userdef.add(5)

# print(Userdef.__hiddenValue) # we cant do this
