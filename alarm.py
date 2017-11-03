#!/usr/bin/python
import time, winsound
while True:
    print "1 - Timer (countdown)"
    print "2 - Convert minutes to seconds"
    print "Custom alarm sound - name it alarm.wav in the root"
    inpit = raw_input("Enter your option:> ")
    if inpit == "1":
        print "Selected 1"
        timer1 = raw_input("Enter timer amount in seconds:> ")
        print "Started"
        time.sleep(int(timer1))
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
    elif inpit == "2":
        print "Selected 2"
        inpit2 = raw_input("Converting minutes to seconds(type 0 to return to menu):> ")
        inpit2 = int(inpit2)
        calculate = inpit2*60
        print "That is "+str(calculate)+" seconds"    
    else:
        print "Invalid input"
