import pandas as pd
import numpy as np

class Demo:
    def __init__(self):
        self.temperature = {}
        self.week = ['Jan 1','Jan 2','Jan 3','Jan 4','Jan 5','Jan 6','Jan 7','Jan 8','Jan 9','Jan 10']

    def create_DS(self):
        with open(r"C:\Users\rosha\OneDrive\Desktop\nyc_weather.csv","r") as f:
            next(f)
            for line in f:
                ele = line.split(',')
                day = ele[0]
                price = float(ele[1])
                self.temperature[day] = price
    
    def get_avgtemp_week(self):
        sum = 0
        for key,val in self.temperature.items():
            if key in self.week:
                sum += val
        avg = sum/len(self.week)
        return avg
        
    def get_max_temp(self):
        max = 0
        for key,val in self.temperature.items():
            if max < val:
                max = val
        return max
        
d = Demo()
        
d.create_DS()
print(d.get_avgtemp_week())
print(d.get_max_temp())
print(d.temperature['Jan 9'])
print(d.temperature['Jan 4'])