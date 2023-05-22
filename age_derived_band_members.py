"""
Purpose: Create a derived class that takes the bands ticket sales and adds their age to see if age effects ticket sales
Author: Anythony Schomer
"""
#Import band members ages
from Band_tickets_class import Band_tickets

#import logger class
from util_datafun_logger import setup_logger

#defining derived class
class Band_tickets_class (Band_tickets):

    def __init__(self, name, points, data, age):
        super().__init__(name, points, data)

        self.age = age

    def __str__(self):
        #Returns a string representation of the instantiated object

        str = f"NumericSeries with name={self.name}, age={self.age} years old, units={self.points}, and {len(self.data)} data points: {self.data}"
        return str