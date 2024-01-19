# class Person:
#     status = 'is alive'
#
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
# p1 = Person(43, 'Alex')
# print(p1.age, p1.name, p1.status)
# p2 = Person(24, 'Vera')
# print(p2.age, p2.name)
# print(p1.__dict__)
# print(p2.__dict__)
# print(Person.__dict__)


# class Person:
#
#     def set_date(self, age, name):
#         self.age = age
#         self.name = name
#
# p1 = Person()
# p1.set_date(11, 'Juliana')
# print(p1.__dict__)
# p2 = Person()
# print(p2.__dict__)

# class Person:
#     status = 'is alive'
#
#     def __init__(self, name, age, height, gender):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.gender = gender
#         self.position = self.determine_position()
#
#     def determine_position(self):
#         if self.age < 18 and self.height < 160:
#             return 'small girl'
#         else:
#             return 'adult'
#
#     def get_date(self):
#         print(f'{Person.status} {self.name.capitalize()} is {self.age} years old is {self.height} cm tall is {self.gender} is {self.position}')
#
#
# person1 = Person('alex', 43, 165, 'mail')
# person1.get_date()
#
# person1 = Person('vera', 39, 165, 'femail')
# person1.get_date()
#
# person1 = Person('veronika', 19, 160, 'femail')
# person1.get_date()
#
# person1 = Person('diana', 13, 155, 'femail')
# person1.get_date()
#
# person1 = Person('Juliana', 11, 150, 'femail')
# person1.get_date()

'''
class Dog:
    def __init__(self, color, age):
        self.color = color
        self.age = age

dog = Dog('black', 5)
'''



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('alex', 43)
# print(p1.__dict__)

'''
import  math

class Circum:

    def __init__(self, radius):
        self.radius = radius

    def calc_square(self):
        return math.pi * self.radius ** 2

my_circ = Circum(6)

print(my_circ.calc_square())
'''








