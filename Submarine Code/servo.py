import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)


while True: # Run forever
   #x=input() #comment this line if you want to use the button
   input_state = GPIO.input(12)
   if input_state == False:
        SetAngle(169)
        print ('bro')      
   else:
       SetAngle(1)

pwm.stop()
GPIO.cleanup()
