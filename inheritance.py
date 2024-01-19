
# class Building:
#     year = None
#     city = None
#     country = None
#     def __init__(self, year, city, country):
#         self.year = year
#         self.city = city
#         self.country = country
#
#     def get_data(self):
#         print(self.year, self.city, self.country)
#
#
# class School(Building):
#
#     def __init__(self, pupils, status, open, year, city, country):
#         super(School, self).__init__(year, city, country)
#         self.pupils = pupils
#         self.status = status
#         self.open = open
#     def get_data(self):
#         super().get_data()
#         print(self.pupils, self.status, self.open)
#
#
# school = School(300, 'basik', True, 1100, 'Kiew', 'Ukraina')
# school.get_data()


# class Person:
#
#     def breathe(self):
#         print('person breathes')
#
#     def sleep(self):
#         print('person sleeps')
#
#     def combo(self):
#         self.breathe()
#         if hasattr(self, 'walk'):
#             self.walk()
#         self.sleep()
#         print(self.age)
# class Doctor(Person):
#
#     age = 30
#
#     def breathe(self):
#         print('person breathes')
#
#     def sleep(self):
#         print('doctor sleeps')
#
#     def walk(self):
#         print('doctor walks')
#
#
# p = Person()
# #p.breathe()
# #p.combo()
# print()
# d = Doctor()
# d.combo()
# d.age


'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(self.num_doors)


class Motorcycle(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model)
        self.num_wheels = num_wheels


    def display_info(self):
        super().display_info()
        print(self.num_wheels)


car = Car('Mazda', 'sx5', 5)
car.display_info()
bike = Motorcycle('suzuki', 'pr22', 2)
bike.display_info()

'''


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print(self.name, self.age)
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def display_info(self):
#         super().display_info()
#         print(f'student id: {self.student_id}')
#
#
# class Employee(Person):
#     def __init__(self, name, age, employee_id):
#         super().__init__(name,age)
#         self.employee_id = employee_id
#
#     def display_info(self):
#         super().display_info()
#         print(f'employee id: {self.employee_id}')
#
#
# student = Student('Alex', 43, 'DCI')
# student.display_info()
#
# employee = Employee('Vera', 39, '45Grad')
# employee.display_info()

'''
class Animal():

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, breed, owner ):
        super().__init__(name, 'gaff')
    
        self.breed = breed
        self.owner = owner


    def get_info(self):
        print(self.name, self.breed, self.owner)


    def make_sound(self):
        print(f'i sey: {self.sound}')


class Cat(Dog, Animal):
    def __init__(self, name, sound, breed, owner, age, has_home):
        super().__init__(name, sound, breed, owner)
        self.breed = breed
        self.owner = owner
        self.age = age
        self.has_home = has_home

    def get_info(self):
        print(self.name, self.breed, self.owner, self.age, self.has_home)

    def make_sound(self):
        print(f'i sey: {self.sound}')



dog = Dog('Jimmy', 'gaff', 'labrador', 'Alex')
dog.get_info()
dog.make_sound()

cat = Cat('Barcic', 'maw', 'British', 'Tanya', 5, True)
cat.get_info()
cat.make_sound()
'''
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#
#     def make_sound(self):
#         print(self.sound)
#
#
# class Pet(Animal):
#     def __init__(self, name, sound, breed=None, owner=None):
#         super().__init__(name, sound)
#         self.breed = breed
#         self.owner = owner
#
#     def get_info(self):
#         print(f"Name: {self.name}, Sound: {self.sound}, Breed: {self.breed}, Owner: {self.owner}")
#
#
# class Dog(Pet):
#     def __init__(self, name, owner):
#         super().__init__(name, 'gaff', breed='Unknown', owner=owner)
#
#
# class Cat(Pet):
#     def __init__(self, name, age, has_home):
#         super().__init__(name, 'maw')
#         self.age = age
#         self.has_home = has_home
#
#     def get_info(self):
#         super().get_info()
#         print(f"Age: {self.age}, Has Home: {self.has_home}")
#
#
# class Cow(Pet):
#     pass
#
# cow = Cow('Burenca', 10, 'Vasya')
# cow.get_info()
# cow.make_sound()
#
# # Пример использования:
# dog = Dog('Jimmy', 'Alex')
# dog.get_info()
# dog.make_sound()
#
# cat = Cat('Barcic', 5, True)
# cat.get_info()
# cat.make_sound()


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f'{self.name} make sound')
#
# class Dog(Animal):
#     def bark(self):
#         print(f'{self.name} barks: Gaw-gaw!!!')


# animal = Animal('som animal')
# dog = Dog('Jimmy')
#
# animal.speak()
# dog.speak()
# dog.bark()
'''
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f'{self.name} make sound')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f'{self.name}, my {self.breed} barks: Gaw-gaw!!!')


animal = Animal('som animal')
dog = Dog('Jimmy', 'Labrador')

animal.speak()
dog.speak()
'''


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return (f'{self.name} {self.age}')


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student = student_id

    def display_info(self):
        return (f'{self.name} {self.age} {self.student}')


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#
#     def display_info(self):
#         return (f'{self.name} {self.age} {self.subject}')


person = Person('Cris', 30)
student = Student('Alex', 43, 'DCI')
#teacher = Teacher('Hassan', 35, 'python')

people = [
    person,
    student,
    #teacher
]

for i in people:
    print(i.display_info())


# person.display_info()
# student.display_info()
# teacher.display_info()
'''
'''
dci_students = [
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
    {'David': {'age': 28, 'id': 'dci'}},
    {'Eva': {'age': 35, 'id': 'dci'}},
    {'Frank': {'age': 22, 'id': 'dci'}},
    {'Grace': {'age': 30, 'id': 'dci'}},
    {'Hank': {'age': 27, 'id': 'dci'}},
    {'Ivy': {'age': 32, 'id': 'dci'}},
    {'Jack': {'age': 29, 'id': 'dci'}},
    {'Karen': {'age': 31, 'id': 'dci'}},
    {'Liam': {'age': 24, 'id': 'dci'}},
    {'Mia': {'age': 26, 'id': 'dci'}},
    {'Nathan': {'age': 33, 'id': 'dci'}},
    {'Olivia': {'age': 28, 'id': 'dci'}},
    {'Peter': {'age': 23, 'id': 'dci'}},
    {'Quinn': {'age': 29, 'id': 'dci'}},
    {'Rachel': {'age': 30, 'id': 'dci'}},
    {'Simon': {'age': 32, 'id': 'dci'}},
    {'Tina': {'age': 27, 'id': 'dci'}}
]
'''
# students_list = []
#
# for item in dci_students:
#     # print(item)
#     for i, j in item.items():
#         age = j['age']
#         student_id = j['id']
#         student_info = i, age, student_id
#         students_list.append(student_info)
# print(students_list)


# i_list = []
#
# for item in dci_students:
#     for i in item:
#         i_list.append(i)
# print(len(i_list))

dci_students = [
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
    {'David': {'age': 28, 'id': 'dci'}},
    {'Eva': {'age': 35, 'id': 'dci'}},
    {'Frank': {'age': 22, 'id': 'dci'}},
    {'Grace': {'age': 30, 'id': 'dci'}},
    {'Hank': {'age': 27, 'id': 'dci'}},
    {'Ivy': {'age': 32, 'id': 'dci'}},
    {'Jack': {'age': 29, 'id': 'dci'}},
    {'Karen': {'age': 31, 'id': 'dci'}},
    {'Liam': {'age': 24, 'id': 'dci'}},
    {'Mia': {'age': 26, 'id': 'dci'}},
    {'Nathan': {'age': 33, 'id': 'dci'}},
    {'Olivia': {'age': 28, 'id': 'dci'}},
    {'Peter': {'age': 23, 'id': 'dci'}},
    {'Quinn': {'age': 29, 'id': 'dci'}},
    {'Rachel': {'age': 30, 'id': 'dci'}},
    {'Simon': {'age': 32, 'id': 'dci'}},
    {'Tina': {'age': 27, 'id': 'dci'}},
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
    {'David': {'age': 28, 'id': 'dci'}},
    {'Eva': {'age': 35, 'id': 'dci'}},
    {'Frank': {'age': 22, 'id': 'dci'}},
    {'Grace': {'age': 30, 'id': 'dci'}},
    {'Hank': {'age': 27, 'id': 'dci'}},
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
    {'David': {'age': 28, 'id': 'dci'}},
    {'Eva': {'age': 35, 'id': 'dci'}},
    {'Frank': {'age': 22, 'id': 'dci'}},
    {'Grace': {'age': 30, 'id': 'dci'}},
    {'Hank': {'age': 27, 'id': 'dci'}},
    {'Nathan': {'age': 33, 'id': 'dci'}},
    {'Olivia': {'age': 28, 'id': 'dci'}},
    {'Peter': {'age': 23, 'id': 'dci'}},
    {'Quinn': {'age': 29, 'id': 'dci'}},
    {'Rachel': {'age': 30, 'id': 'dci'}},
    {'Simon': {'age': 32, 'id': 'dci'}},
    {'Tina': {'age': 27, 'id': 'dci'}},
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
    {'Nathan': {'age': 33, 'id': 'dci'}},
    {'Olivia': {'age': 28, 'id': 'dci'}},
    {'Peter': {'age': 23, 'id': 'dci'}},
    {'Quinn': {'age': 29, 'id': 'dci'}},
    {'Rachel': {'age': 30, 'id': 'dci'}},
    {'Simon': {'age': 32, 'id': 'dci'}},
    {'Tina': {'age': 27, 'id': 'dci'}},
    {'Alex': {'age': 43, 'id': 'dci'}},
    {'Bob': {'age': 40, 'id': 'dci'}},
    {'Charlie': {'age': 25, 'id': 'dci'}},
]

# def len_list(som_list):
#     i_list = []
#
#     for item in som_list:
#         for i in item:
#             i_list.append(i)
#     print(len(i_list))
#
# len_list(dci_students)

def count(sum_list, sum_name):
    count = 0
    name = sum_name
    name_found = False
    for item in sum_list:
        for i in item:
            if name == i:
                count += 1
                name_found = True

    if name_found:
        print(count, name)

    else:
        print('There no surch name')

count(dci_students, 'Frank')


