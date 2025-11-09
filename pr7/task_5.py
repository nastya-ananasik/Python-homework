from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned ON")

    def turn_off(self):
        print("LightBulb: turned OFF")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: started spinning")

    def turn_off(self):
        print("Fan: stopped spinning")

class ElectricSwitch:
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True

bulb = LightBulb()
fan = Fan()

switch_for_bulb = ElectricSwitch(bulb)
switch_for_bulb.press()

switch_for_fan = ElectricSwitch(fan)
switch_for_fan.press()
