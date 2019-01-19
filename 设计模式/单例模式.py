class MyBeautifulGril(object):
    """我的漂亮女神"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + "，我一见钟情！")
            MyBeautifulGril.__isFirstInit = True
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")


# 各种singleton实现方式
########################################################################################################################
class Singleton1(object):
    """单例实现方式一"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True

    def getName(self):
        return self.__name

# # # Test
# tony = Singleton1("Tony")
# karry = Singleton1("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


# 方式二
#========================================================================================
class Singleton2(type):
    """单例实现方式二"""

    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None # 初始化全局变量cls._instance为None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程，如果cls._instance为None则创建，否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class CustomClass(metaclass=Singleton2):
    """用户自定义的类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


tony = CustomClass("Tony")
karry = CustomClass("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)


# 方式三
#========================================================================================
def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器"""
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton


@singletonDecorator
class Singleton3:
    """使用单例装饰器修饰一个类"""

    def __init__(selfself, name):
        self.__name = name

    def getName(selfself):
        return self.__name


# tony = Singleton3("Tony")
# karry = Singleton3("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


# Version 2.0
########################################################################################################################
@singletonDecorator
class MyBeautifulGril(object):
    """我的漂亮女神"""

    def __init__(selfself, name):
        self.__name = name
        if self.__name == name:
            print("遇见" + name + "，我一见钟情！")
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(selfself):
        print(self.__name + "就我心中的唯一！")


# Test
########################################################################################################################
# def TestLove():
#     jenny = MyBeautifulGril("Jenny")
#     jenny.showMyHeart()
#     kimi = MyBeautifulGril("Kimi")
#     kimi.showMyHeart()
#     print("id(jenny):", id(jenny), " id(kimi):", id(kimi))
# 
#
# TestLove()

"""
使用装饰器
"""
# def singleton(cls):
#     __instance = {}
#     def _singleton(*args, **kwargs):
#         if cls not in __instance:
#             __instance[cls] = cls(*args, **kwargs)
#         return __instance[cls]
#     return _singleton
#
# @singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self._x = x
#
# a = A(2)
# b = A(3)
# print(a, a.__dict__)
# print(b, b.__dict__)
# print(b._x)

"""
    使用类
"""
# class Singleton(object):
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = cls(*args, **kwargs)
#         return cls._instance
#
# a = Singleton().instance()
# b = Singleton().instance()
# print(a, b)

# """
#     多线程测试
# """
# import threading
#
# class Singleton(object):
#
#     __instance_lock = threading.Lock()
#     def __init__(self):
#         import time
#         time.sleep(1)
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         with Singleton.__instance_lock:
#             if not hasattr(cls, '_instance'):
#                 cls._instance = cls(*args, **kwargs)
#             return cls._instance
#
#
# def task(arg):
#     s = Singleton.instance()
#     print(s)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=[i,])
#     t.start()


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            print(s.split(2))
#
# if __name__ == '__main__':
#     unittest.main()

import unittest


def calc(expression):
    return eval(expression)


def add_test(name, asserts):
    def test_method(asserts):
        def fn(self):
            left, right = asserts.split('=')
            expected = str(calc(left))
            self.assertEqual(expected, right)

        return fn

    d = {'test1': test_method(asserts)}
    cls = type(name, (unittest.TestCase,), d)
    globals()[name] = cls


if __name__ == '__main__':
    for i, t in enumerate([
        "1+2=3",
        "3*5*6=90"]):
        add_test("Test%d" % i, t)
    unittest.main()

