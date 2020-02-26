from __future__ import print_function
import time
import dual_g2_hpmd_rpi
from dual_g2_hpmd_rpi import motors, MAX_SPEED       
from time import sleep
import keyboard
import time

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)
    if motors.motor2.getFault():
        raise DriverFault(2)
    if motors.motor3.getFault():
        raise DriverFault(3)
    if motors.motor4.getFault():
        raise DriverFault(4)

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]  

motors.setSpeeds(0, 0)

print("\n")
print("Created by Aaron Smith and Thomas McDonald")
print("w- forward full speed\ne- forward halfspeed\ns- back full speed\nd- back halfspeed\nb- bilge\np- pitch")
print("\n")

shiftcounter = 0
speedvar = MAX_SPEED
halfspeed = (MAX_SPEED*.5)

    
while True:  # making a loop  

    try:
        #Back
        if keyboard.is_pressed("s"):  # if key 's' is pressed 
            #print("\n forward (s)")
            motors.enable()
            motors.motor1.setSpeed(MAX_SPEED)
            motors.motor2.setSpeed(MAX_SPEED)
            raiseIfFault()
        
        #back halfspeed
        elif keyboard.is_pressed("d"):  # if key 's' is pressed 
            #print("\n forward (s)")
            motors.enable()
            motors.motor1.setSpeed(halfspeed)
            raiseIfFault()

        #Forward
        elif keyboard.is_pressed("w"):
            #print("\n backward (w)")
            motors.enable()
            motors.motor2.setSpeed(-MAX_SPEED)
            motors.motor1.setSpeed(-MAX_SPEED)
            raiseIfFault()
        
        #Forward halfspeed
        elif keyboard.is_pressed("e"):
            #print("\n backward (w)")
            motors.enable()
            motors.motor1.setSpeed(-halfspeed)
            raiseIfFault()
       
        elif keyboard.is_pressed("p"):
            #print("\n backward (w)")
            motors.enable()
            motors.motor2.setSpeed(MAX_SPEED)
            raiseIfFault()
       
        elif keyboard.is_pressed("b"):
            #print("\n backward (w)")
            motors.enable()
            motors.motor2.setSpeed(MAX_SPEED)
            raiseIfFault()
            
        #Stop
        else:
            #print("\n no input")
            motors.disable()
    except:
        #print("shouldn't see this")
        #break  # if user pressed a key other than the given key,  break
        time.sleep(0.05)

