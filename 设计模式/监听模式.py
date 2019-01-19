# class WaterHeater:
#     "热水器：战胜寒冬的有利武器"
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25
#     def getTemperature(self):
#         return self.__temperature
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("current temperature is:", self.__temperature)
#         self.notifies()
#     def addObserver(self, observer):
#         self.__observers.append(observer)
#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)
# class Observer:
#     "洗澡模式和饮用模式的父类"
#     def update(self, waterHeater):
#         pass
# class WashingMode(Observer):
#     "该模式用于洗澡用"
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
#             print("水已烧好，温度正好！可以用来洗澡了。")
# class DrinkingMode(Observer):
#     "该模式用于饮用"
#     def update(self, waterHeater):
#             if waterHeater.getTemperature() >= 100:
#                 print("水b已烧开！可以用来饮用了。")
#
#
# def testWaterHeater():
#     heater = WbaterHeater()
#     washingObser = WashingMode()
#     drinkingObser = DrinkingMode()
#     heater.addObserver(washingObser)
#     heater.addObserver(drinkingObser)
#     heater.setTemperature(40)
#     heater.setTemperature(60)
#     heater.setTemperature(100)
#
#
# class Observer:
#     "观察者的基类"
#     def update(self, observer, object):
#         pass
# class Observable:
#     "被观察者的基类"
#     def __init__(self):
#         self.__observers = []
#     def addObserver(self, observer):
#         self.__observers.append(observer)
#     def removeObserver(self, observer):
#         self.__observers.remove(observer)
#     def notifyObservers(self, object=0):
#         for o in self.__observers:
#             o.update(self, object)
#
#
# class WaterHeater(Observable):
#     "热水器：战胜寒冬的有利武器"
#     def __init__(self):
#         super().__init__()
#         self.__temperature = 25
#     def getTemperature(self):
#         return self.__temperature
#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("current temperature is:", self.__temperature)
#         self.notifyObservers()
# class WashingMode(Observer):
#     "该模式用于洗澡用"
#     def update(self, observable, object):
#         if isinstance(observable,WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
#             print("水已烧好，温度正好！可以用来洗澡了。")
# class DrinkingMode(Observer):
#     "该模式用于饮用"
#     def pupdate(self, observable, object):
#         if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
#             print("水已烧开！可以用来饮用了。")






































#
# class WaterHeater:
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25
#     def get_temperature(self):
#         return self.__temperature
#     def set_temperature(self, temparature):
#         self.__temperature = temparature
#         print('现在温度是:', self.__temperature)
#         self.notifies()
#     def add_observer(self, observer):
#         self.__observers.append(observer)
#     def remove_observer(self, observer):
#         self.__observers.remove(observer)
#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)
#
# class Observer:
#     def update(self, waterHeater):
#         pass
#
# class HeatMode(Observer):
#     def update(self, waterHeater):
#         if waterHeater.get_temperature() > 40 and waterHeater.get_temperature() < 70:
#             print('可以洗澡了')
#
# class DrinkMode(Observer):
#     def update(self, waterHeater):
#         if waterHeater.get_temperature() > 100:
#             print('可以喝水了')
#
# heater = WaterHeater()
# heatMode = HeatMode()
# drinkMode = DrinkMode()
# heater.add_observer(heatMode)
# heater.add_observer(drinkMode)
# heater.set_temperature(50)
# heater.set_temperature(101)


class Observer():
    """观察者基类"""
    def update(self, observer, object):
        pass

class Observerable():
    """ 被观察者基类"""
    def __init__(self):
        self.__observers = []
    def add_observer(self, observer):
        self.__observers.append(observer)
    def remove_observer(self, observer):
        self.__observers.remove(observer)
    def notifies(self, object=0):
        for o in self.__observers:
            o.update(self, object)

class WaterHeater(Observerable):
    def __init__(self):
        super().__init__()
        self.__temparature = 25
    def get_temperature(self):
        return self.__temparature
    def set_temperature(self, temperature):
        self.__temparature = temperature
        self.notifies()

class HeatMode(Observer):
    def update(self, waterHeater, object):
        if isinstance(waterHeater, WaterHeater) and waterHeater.get_temperature() > 40 and waterHeater.get_temperature() < 70:
            print('可以洗澡了哟!')

class DrinkMode(Observer):
    def update(self, waterHeater, object):
        if isinstance(waterHeater, WaterHeater) and waterHeater.get_temperature() > 100:
            print('可以喝水了')





heater = WaterHeater()
heatMode = HeatMode()
drinkMode = DrinkMode()
heater.add_observer(heatMode)
heater.add_observer(drinkMode)
heater.set_temperature(50)
heater.set_temperature(101)
