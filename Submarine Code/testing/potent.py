from gpiozero import MCP3008
from time import sleep
import time

while True:
    with MCP3008(channel=0) as pot:
        potdat = pot.value * 15
        print(pot.value)
        
        
    time.sleep(0.05)