import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
in3 = 18
in4 = 16
en = 22
temp1=1

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.setup(in1,GPIO.OUT)
#GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,1000)
p.start(22)

#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)



while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        print("forward")
        
    else:
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)