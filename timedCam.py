#!/usr/bin/python3

import time
import picamera

#runCountDown takes an int representing seconds, and converts it to minutes. Then shows the countdown once a minute
def runCountDown(seconds):
    minutes = seconds / 60
    minutes = int(minutes)
    for i in range(minutes):
        print(minutes)
        minutes -= 1
        time.sleep(60)
        

with picamera.PiCamera() as camera:
    camera.start_preview(fullscreen = False, window = (100,20,640, 480))
    val = input("How long should the camera stay on? ")
    secondsOn = int(val)
    displayTime = secondsOn/60
    print("Cam will be on for " + str(displayTime) + " minutes" )
    
    countDownBool = input("Do you want a count down? y/n ")
    if countDownBool == 'y':
        runCountDown(secondsOn)
        time.sleep(2)
    else:
        time.sleep(secondsOn)
    camera.stop_preview()
    
