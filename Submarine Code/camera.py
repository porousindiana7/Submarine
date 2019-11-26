import time
import picamera
import os
#os.system('mpg321 B6GD.mp3 &')


camera = picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(60)
    camera.stop_preview()
finally:
    camera.close()
  
