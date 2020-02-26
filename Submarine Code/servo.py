import RPi.GPIO as GPIO



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
    with MCP3008(channel=1) as pot1:
        potdat1 = round((pot1.value * 10), 2)
        print(potdat1)
        p1.ChangeDutyCycle(potdat1)
        
    with MCP3008(channel=0) as pot:
        potdat = round((pot.value * 10), 2)
        print(potdat)
        p.ChangeDutyCycle(potdat)
        
#time.sleep(0.05)

p.stop()
GPIO.cleanup()
