
class Temperature() :
    def __init__(self, celcius):
        self.celcius = celcius

        @property
        def fahrenheit(self):
            return self.celcius * 9 / 5 + 32

        @fahrenheit.setter
        def fahrenheit(self, value)
            self.celcius = (value - 32) * 5 / 9


temp = Temperature(5)
var = temp.fahrenheit

temp.fahrenheit = 32
temp.celsius
