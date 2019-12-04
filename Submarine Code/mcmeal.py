import RPi.GPIO as GPIO          
from time import sleep
import keyboard
import time

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while True:  # making a loop
    try:
        #Slow Forward
        if keyboard.is_pressed("w"):  # if key 'w' is pressed 
            print("\n forward (w)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
        
        #Slow Back
        elif keyboard.is_pressed("s"):
            print("\n backward (s)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)      
        
        #Stop
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            print("\n no input")   
    except:
        print("shouldn't see this")
        #break  # if user pressed a key other than the given key,  break
    time.sleep(0.05)
