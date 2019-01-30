'''
IBEHS 1P10
Project Three: Track and Field
Group 22 - TO4
UV Monitoring Sunglasses to Prevent Sunburns
Wednesday, February 28, 2018
'''

#Import Libraries
import time
import os
from time import sleep
import RPi.GPIO as GPIO
import PCF8591 as ADC

#UV Sensor
#Turn off warning about dual-initializing output pin
GPIO.setwarnings(False)
ADC.setup(0x48)

#Functions

#Take reading from UV Photodiode Sensor
def getReading():
    output = ADC.read(0) #UV index readings as output variable
    print(output)           
    return output

#Determine appropriate amount of time to spend in the sun, set appropriate countdown
def getMaxTime(l):
    print('Finding a new max exposure time')
    #Take average of collected data points
    avgValue = sum(l)/len(l)
    #Countdown values are minimized for testing efficiency
    #UV Ranges are based off of UV index chart (see appendix of Technical Report)
    if 0 <= avgValue <= 4:      
        countdown = 6*60
    elif 4 < avgValue <= 6:     
        countdown = 4*60
    elif 6 < avgValue <= 8:     
        countdown = 3*60
    elif 8 < avgValue <= 10:
        countdown = 2*60 
    elif avgValue > 10:         
        countdown = 1*60
    print('The maximum amount of time they can remain in the sun has been updated to:',countdown,'seconds') 
    return countdown            

#Five minute warning buzz, buzzes for 4 seconds
def fivebuzz():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5,1)
    time.sleep(4)               
    GPIO.output(5,0)
    time.sleep(1)
    GPIO.cleanup()


#Final buzz statement, buzz indefinitely when timer runs out (set with sleeps and exits program for testing purposes)
def buzz():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5,1)        
    time.sleep(5)
    GPIO.output(5,0)
    print("All Done!")
    exit()  

def Main():
    Time = 0
    #Set max time greater than maximum possible countdown amount
    maxTime = 10 * 60
    data = []
    while Time < maxTime:       
        print('The timer has been running for:',Time,'seconds')
        #1 second instead of 10, for testing efficiency
        sleep(1.0)
        #Increase time by 10 seconds to indicate time passage
        Time += 10
        #Append data readings to list
        data.append(getReading())
        print(data)
        #At every 2 minute interval, take UV average and set OR update timer appropriately
        if Time % 120 == 0:
            maxTime = getMaxTime(data)
        print('The amount of time they can remain in the sun is:', maxTime - Time,'seconds')
        #Range set for testing. Buzz once when 5 minutes are left on timer as warning
        if 4*60 <= maxTime - Time <= 5*60:
            print('Less than 5 minutes remaining')
            fivebuzz()
    #Buzz indefinitely when countdown reaches zero
    while True:
        buzz()

Main()
