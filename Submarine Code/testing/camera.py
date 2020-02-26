import time
import picamera
import os
#os.system('mpg321 B6GD.mp3 &')


camera = picamera.PiCamera()
try:
    camera.start_preview()
    camera.rotation = 180
    time.sleep(2000)
    camera.stop_preview()
finally:
    camera.close()
    
