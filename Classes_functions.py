# class A:
#
#     def hello():
#         return 'Hello'
#
#     def world():
#         return 'world'
#
# print(A.hello() +' '+A.world())

'''
class Dog:

    def send_bark(self):
        print('WOOF! I MMA BIT YOU')


dog = Dog()
dog.send_bark()
Dog.send_bark(dog)
'''

# class B:
#
#     def calc_sum(self, num_1, num_2):
#         print(num_1 + num_2)
#
# summ = B()
# summ.calc_sum(25,25)

# class Product:
#
#     title: str = 'chocolate'
#     price: int = 52
#
#
# Product.amount: int = 20
#
# print(Product.__dict__)


import pprint

'''
class Person:
    name = 'Alex'
    age = 43

setattr(Person, 'hear_color', 'fier')
setattr(Person, 'weight', 75)

pprint.pprint(Person.__dict__)


getattr(Person, 'weight', 'no')
delattr(Person, 'weight')

pprint.pprint(Person.__dict__)
'''
# import  math
# class Computer:
#
#
#     age: int = 2
#     price: int = 1000
#     size: str = 'big'
#
#
# # setattr(Computer, 'pi', 'saf')
# #
# # pprint.pprint(Computer.__dict__)
# print(getattr(Computer, 'sdf', str(math.pi)))
#
# print()
#
# delattr(Computer, 'age')
#
# pprint.pprint(Computer.__dict__)
#

'''
class Person:
    name = 'Alex'
    age = 43


p1 = Person()
p1.height = 165

print(getattr(Person, 'height', False))
print(isinstance(p1, type), isinstance(p1, int), sep='\n')
'''

# class Person:
#     def send():
#         pass
#
# Person.age = 5
# p1 = Person()
# print(p1.__dict__)
# print(Person.send)

'''
class Number:

    def sum(self, num1, num2):
        result = num1 + num2
        return result

num = Number()
print(num.sum(4, 4))
'''


