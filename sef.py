# class A:
#     def set_num(self):
#         self.x = 20
#
# a = A()
# a.set_num()
# print(a.__dict__)
# b = A()
# print(b.__dict__)

class MyClass:

    def two_atr(self, x, y):
        self.x = x
        self.y = y


    def sum_atr(self):
        return self.x + self.y
    

c = MyClass()
c.two_atr(2, 2)
result = c.sum_atr()

print(result)