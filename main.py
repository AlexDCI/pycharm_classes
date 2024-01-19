import random


class PersianCat:
    breed = 'persian' # attribute of this class
    age = 12.0


class SiberianCat:
    breed = 'siberian'
    age = 0.5


class BengalCat:
    breed = 'bengal'
    age = 2.0


# tom = PersianCat()
# print(tom.age)
# print(PersianCat.age)
# tom.legs = 4
# print(tom.legs)
# print(tom.__dict__)


garfield = SiberianCat()
maxim = BengalCat()

# print(type(tom), type(garfield), type(maxim), sep='\n')


# isinstance() проверяет принадлежность какому либо классу
# print(isinstance(tom, BengalCat))
# getattr() функция предназначена для получения атрибута класса
# delattr() удаляет класс
# setattr() устанавливает значение для значения класса


class Person:
    age = 43
    height = 175


alex = Person()
alex.color_hear = 'black'
alex.height = 165


hasan = Person()
hasan.color_hear = 'braun'

# print(f'{alex.__dict__} alex age {alex.age} years {hasan.__dict__} hasans age { hasan.age} hasan height {hasan.height}', sep='\n')








# print(getattr(Person, 'legs', 2))
# setattr(Person, 'arms', 'long')
# print(Person.arms)


class A:
    a = 2
    b = 2

# print(getattr(A, 'a') + getattr(A, 'b'))

class B:
    pass


# setattr(B, 'y', 12)
# B.y = 'hallo world'
# print(getattr(B, 'y').upper())
# print(B.__dict__)

class C:
    x = 20
    y = 10


# del C.y
# print(getattr(C, 'y', 'is deleted'))
# delattr(C, 'x')
#
# print(C.__dict__)


# class Cat:
#     breed = 'forest'
#     age = 2
#
#
# print(getattr(Cat, 'breed'), getattr(Cat, 'age'))
#
# my_cat = Cat()
# setattr(my_cat, 'age', 5)
# print(my_cat.age)


# class Car:
#     speed: float = 100.0
#     color: str = 'black'
#
#
# print(Car.speed, Car.color)
#
# del Car.speed
# print(Car.__dict__)

class Dog:
    name = None
    color = None
    age = None
    breed = None

'''
    def set_data(self, name, color, age, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

    def get_data(self):
        print(self.name, 'is',self.color, 'it is', self.age, 'years old', 'a breed is', self.breed)


my_dog = Dog()
my_dog.set_data('Jimmy', 'black', 4, 'labrador')
my_dog.get_data()
'''
# class FirstClass:
#     x = 'x'
#
#
# setattr(FirstClass, 'y', 'y')
#
# new_exsempl = FirstClass()
# new_exsempl.y = 'y'
# print(FirstClass.__dict__)
# print(new_exsempl.__dict__)

'''
import math


class Circle:
    radius: float = 5.


class Rectangle:
    width: float = 5.
    height: float = 7.

print(math.pi*Circle.radius**2)
print()
print(Rectangle.width*Rectangle.height)
'''

# class Man:
#     height = 175
#     weight = 65
#     amount: int = 150
#     year: int = 2020
#
#
# Man.year += 1
# Man.amount -= 2
# # print(Man.__dict__)
#
#
# class Cat:
#     color: str = 'white'
#     amount = 14
#
#
# arr = [Cat() for _ in range(14)]
# arr[0].color = arr[1].color = 'black'
# print(arr[0].color, arr[1].color, arr[7].color)


# import pprint
#
# pprint.pprint(tuple.__dict__)

'''
class School:
    age: int = 15
    height: int = 160
    amount: int = 5

    def set_data(self, age, height, amount):
        self.age = age
        self.height = age
        self.amount = amount

    def get_date(self):
        print(self.age, self.height, self.amount)


boy = [School() for _ in range(5)]
print(School.amount)
boy[0].height = 165
print(boy[0].height, boy[1].height)
School.amount -= 1
print(School.amount)
boy = School()
print(boy.get_date())
'''
# from pprint import pprint
# from random import randrange
# class Boy:
#     age: int = 15
#     height: int = 160
#
#
# arr = [Boy() for _ in range(5)]
# index = randrange(0, 5)
# arr[index].height = 165
# print(arr[index].__dict__)
# arr_height = [arr[index].height for index in range(5)]
# pprint(arr_height)
#
# boy = random.choice(arr)
# print(boy)
# del boy
# print(boy)
#

'''
languages =['english', 'french', 'deutsch']

class Country:
    population: int = 5e6
    regime: str = 'democracy'
    square: int = 3e5


arr = [Country() for _ in range(3)]
for count, country in enumerate(arr):
    country.languages = languages[count]

print([arr[index].languages for index in range(3)])
'''

