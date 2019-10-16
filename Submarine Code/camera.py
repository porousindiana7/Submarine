import sys
from picamera import PiCamera
from tkinter import *
from tkinter.ttk import *


# Initialize tkinter window with dimensions 100x100

# create a tkinter window
root = Tk()

root.geometry('200x400+1200+300')


camera = PiCamera()

camera.start_preview(fullscreen=False, window = (0, 400, 1000, 720))

# camera.zoom=(x/100.,x/100.,0.5,0.5)

def quitHandler():
    print ("Goodbye")
    root.destroy()
    camera.close()


def callback1():
    print ("end program button clicked")


btn = Button(root, text = 'End Program', width=200, command = quitHandler)

btn.pack(side = 'top')

root.mainloop()
