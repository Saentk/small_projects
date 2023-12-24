
                                # Studying OOP

class Human:                                            

    def __init__(self, name, age, money = 0, house = None):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
        print("\nMeet new human! His name is {}".format(self.name))

    def info(self):
        print('{}, {} years old, money: {}, house: {}'.format(self.name, self.age, self.__money, self.__house))
        
    def working(self, got_money):
        self.__money = self.__money + got_money

    default_discount = 0

    def getting_house(self, house, discount = default_discount):
        if house.used == False:
            price = house.cut_price(discount)
            if self.__money >= price:
                self.__make_deal(house, price)
            else: 
                print('Not enoght money :(')
        else:
            print('House is already bought!')

    def __make_deal(self, house, price):                 # need to make it privat to prevent using it without func getting_house
            house.used = True
            self.__money -= price
            self.__house = house

    def __str__(self):
        return 'Human: {} - {}'.format(self.name, self.age)


class House:
    def __init__(self, name, price, area, used = False):
        self.name = name
        self.price = price
        self.area = area
        self.used = used

    def info(self):
        print('\n{},  price: {}, area: {}, used = {}'.format(self.name, self.price, self.area, self.used))

    def __str__(self):
        return '{}, area: {}'.format(self.name, self.area)

    def cut_price(self, discount):
        p = (100 - discount) / 100
        return round(self.price * p)


class small_house(House):                           # There is a job to make child class 'small house'

    def __init__(self, name, price, garage, area = 30):
        House.__init__(self, name, price, area)
        self.garage = garage

    def info(self):
        House.info(self)
        if self.garage == True:
            print('The house has garage'.format(self.price))
        else:
            print("The house does`n have garage".format(self.price))


    def __str__(self):
        return '{}, area: {}'.format(self.name, self.area)




                                                            # Testing methods
Ord_house = House('ord_house', 35000, 40)
Ord_house1 = small_house('ord1.house', 28000, False)

tom = Human('Tom', 25)
val = Human("Valerii", 22)
val.working(3000)
val.getting_house(Ord_house)
val.info()
tom.working(35000)
tom.getting_house(Ord_house, 10)
tom.info()
Ord_house.info()
print(Ord_house)
