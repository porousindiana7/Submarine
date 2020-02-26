import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
p = GPIO.PWM(17, 50)
p.start(2.5)

GPIO.setup(4,GPIO.OUT)
p1 = GPIO.PWM(4, 50)
p1.start(0)


from gpiozero import MCP3008
#from time import sleep
while True:
    if keyboard.is_pressed("i"):
        p1.ChangeDutyCycle(100)
    elif keyboard.is_pressed("k"):
        p1.ChangeDutyCycle(50)


#time.sleep(0.05)

p.stop()
GPIO.cleanup()