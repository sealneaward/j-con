import APDS9300 as LuxSens
import RPi.GPIO as GPIO
import MPL3115A2 as altibar
import time
from ctypes import *

sensor = CDLL('./libMPL.so')

class Sensor():
    def __init__(self):
	sensor.I2C_Initialize(altibar.MPL3115A2_ADDRESS)        
	self.AltiBar = altibar.MPL3115A2() 

    def get_data(self):
	time.sleep(0.5)
        self.AltiBar.ActiveMode()                                            #puts sensor in active mode
        time.sleep(0.5)
        temperature = self.AltiBar.ReadTemperature()
        time.sleep(0.5)
        self.AltiBar.AltimeterMode()
        time.sleep(0.5)
        altitude =  self.AltiBar.ReadAltitude()              #Take a pressure reading
        time.sleep(0.5)
        self.AltiBar.BarometerMode() #puts sensor in active mode
        time.sleep(0.5)
        baroPressure = self.AltiBar.ReadBarometricPressure()                #Take a pressure reading

        sensorData = {
                'Title' : 'Sensorian Dashboard ',
                'temperature' : temperature,
                'altitude' : altitude/1000,
                'pressure' : baroPressure
                }
	
        return sensorData
