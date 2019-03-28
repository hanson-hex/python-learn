list = (1, 3, 4, 4)
name = 'list'
# print("result:{0}".format(*list))

from functools import wraps

class singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

def singletonDe(cls):
    instance = {}
    def getInstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getInstance


class A(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(A, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
    # def go(self):
    #     print ("go A go!")
    # def stop(self):
    #     print ("stop A stop!")
    # def pause(self):
    #     raise Exception("Not Implemented")
class B(A):
    def go(self):
        print ("go B go!")
class C(singleton):
    def go(self):
        super(C, self).go()
        print ("go C go!")
    def stop(self):
        super(C, self).stop()
        print ("stop C stop!")
@singletonDe
class D():
    def go(self):
        super(D, self).go()
        print ("go D go!")
    def stop(self):
        super(D, self).stop()
        print ("stop D stop!")
    def pause(self):
        print ("wait D wait!")
class E(B,C):
    pass
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
b = D()
print(b)
a = D()
print(a)

