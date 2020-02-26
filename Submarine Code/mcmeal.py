import RPi.GPIO as GPIO          
from time import sleep
import keyboard
import time

#first motors
in1 = 24
in2 = 23

in3 = 4
in4 = 17
#second motor
in5 = 19
in6 = 13

#third motor
in7 = 21
in8 = 20

#en
en = 25
en1 = 26
en2 = 27
en3 = 16
#temp
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)

GPIO.setup(en,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)


p=GPIO.PWM(en,1000)
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)
p3=GPIO.PWM(en3,1000)

p.start(25)
p1.start(26)
p2.start(27)
p3.start(16)

print("\n")
print("Created by Aaron Smith and Thomas McDonald")
print("w-forward, s-backwards, a- left, d- right, r-pitch down, f-pitch up, e-pump")
print("\n")

while True:  # making a loop
    try:
        #Back s
        if keyboard.is_pressed("s"):  # if key 's' is pressed 
            #print("\n backward (s)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            p2.ChangeDutyCycle(100)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)        
        
        #Forward w
        elif keyboard.is_pressed("w"):
            #print("\n forward (w)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            p2.ChangeDutyCycle(100)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW) 
########################################
       
       #right d
        elif keyboard.is_pressed("d"):
            #print("\n right (d)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            p2.ChangeDutyCycle(100)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)             
            
       #left a
        elif keyboard.is_pressed("a"):
            #print("\n left (a)")
            p.ChangeDutyCycle(100)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            p2.ChangeDutyCycle(100)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)


##########################################    
        
        #pitch r
        elif keyboard.is_pressed("r"):
            #print("\n pitch (d)")
            p1.ChangeDutyCycle(100)
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.HIGH)
            
        #pitch a
        elif keyboard.is_pressed("f"):
            #print("\n pitch (a)")
            p1.ChangeDutyCycle(100)
            GPIO.output(in5,GPIO.HIGH)
            GPIO.output(in6,GPIO.LOW)
            
###################################
            
        #pump e
        elif keyboard.is_pressed("e"):
            #print("\n pump (e)")
            p3.ChangeDutyCycle(100)
            GPIO.output(in7,GPIO.HIGH)
            GPIO.output(in8,GPIO.LOW)            
            
            
            
   
###############################  

        #Stop
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.LOW)
            GPIO.output(in7,GPIO.LOW)
            GPIO.output(in8,GPIO.LOW) 
            #print("\n no input")   
    except:
        print("shouldn't see this")
        #break  # if user pressed a key other than the given key,  break
    time.sleep(0.05)
