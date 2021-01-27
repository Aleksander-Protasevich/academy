class Familly:
    legs = 2
    def __init__(self, a = 'Protasevich', b = 'Minsk'):
        self.__surname = a
        self.city = b

    def descr(self, name):
        print(f'{name} {self.surname} lives in {self.city}')

    def job(self, prof):
        self.descr('Dima')
        print(f'{self.surname} is a {prof}')

    

dad = Familly()
print(dad._Familly__surname)
mom = Familly('Kolibabchuk', 'Kyiv')
# print(mom.surname)
son = Familly()
son.age = 15
son.legs = 3
# print(son.legs)
# print(dad.legs)

# son.descr('Tolya')
# mom.descr('Dasha')
# dad.descr('Dima')
# dad.surname = 'Kolibabchuk'
# dad.job('Painter')