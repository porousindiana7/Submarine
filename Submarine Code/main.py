# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
import sys
from picamera import PiCamera
from Tkinter import *
import ttk  
import spidev
import time
import os


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2

# Define delay between readings (s)
delay = .5



# Initialize tkinter window with dimensions 100x100               
root = Tk()    

root.geometry('200x400+1200+300')   


# camera = PiCamera()
# camera.start_preview(fullscreen=False, window = (0, 400, 1000, 720))
# camera.zoom=(x/100.,x/100.,0.5,0.5)



# def quitHandler():
    # print ("Goodbye")
    # root.destroy()
    # camera.close()


def callback1():
    print ("end program button clicked")


import RPi.GPIO as GPIO          
from time import sleep

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


# Joystick

while True:

  # Read the joystick position data
  vrx_pos = ReadChannel(vrx_channel)
  vry_pos = ReadChannel(vry_channel)
  #spdp = (((ReadChannel(vry_channel))/1024)*100.0)

 # Read switch state
  swt_val = ReadChannel(swt_channel)

  # Print out results
  print "--------------------------------------------"
  print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))


  if (vry_pos > 550):
   print("forward")
   GPIO.output(in1,GPIO.HIGH)
   GPIO.output(in2,GPIO.LOW)
   x = 'z'



# Above is forward motor speeds

  elif (vry_pos < 500):
   print("backward")
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.HIGH)
   temp1=0
   x='z'

         
  else:
   print("no y input")
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)
   x='z'






  prct=abs((((vry_pos)/10)-2))
  print(prct)
  p.ChangeDutyCycle(prct)


  # Wait before repeating loop
  time.sleep(delay)



while(1):

    x=raw_input()
    


    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
  #  elif x=='e':
   #     GPIO.cleanup()
    #    print("GPIO Clean up")
     #   break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")







root.mainloop()

