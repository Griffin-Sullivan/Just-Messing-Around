import time
from pygame import mixer
from tkinter import *

#initializing window and widgets
master = Tk()
master.title("Alarm Clock")

hourLab = Label(master, text="Hour:")
hourLab.grid(column=0, row=0)
hourBox = Spinbox(master, from_=0, to=24, width=3)
hourBox.grid(column=1, row=0, ipadx=10)

minLab = Label(master, text="Minute:")
minLab.grid(column=2, row=0)
minBox = Spinbox(master, from_=0, to=60, width=3)
minBox.grid(column=3, row=0, ipadx=10)

secLab = Label(master, text="Second:")
secLab.grid(column=4, row=0)
secBox = Spinbox(master, from_=0, to=60, width=3)
secBox.grid(column=5, row=0, ipadx=10)

def snooze():
    mixer.music.stop()

    #adds 30 seconds to alarm
    cTime = time.strftime("%H:%M:%S", time.localtime())
    secSnooze = time.strftime("%S", time.localtime())
    hourSnooze = time.strftime("%H", time.localtime())
    minSnooze = time.strftime("%M", time.localtime())
    updateSecSnooze = int(secSnooze) + 30

    #adjusts if hour, minute, or second will go over 24 or 60
    if (updateSecSnooze > 60):
        updateSecSnooze = updateSecSnooze - 60
        minSnooze = int(minSnooze) + 1
        
        if (minSnooze >= 60):
            hourSnooze = int(hourSnooze) + 1
            minSnooze-=60
            
            if (hourSnooze >= 24):
                hourSnooze -= 24

    hourSnooze = str(hourSnooze)
    minSnooze = str(minSnooze)
    updateSecSnooze = str(updateSecSnooze)

    #concatenates 0 to get the form '00' if the length is 1
    if (len(hourSnooze) < 2):
        hourSnooze = "0" + hourSnooze
        
    if (len(minSnooze) < 2):
        minSnooze = "0" + minSnooze
          
    if (len(updateSecSnooze) < 2):
        updateSecSnooze = "0" + updateSecSnooze

    #waits for time to reach snooze and plays song
    snoozeAlarm = hourSnooze + ":" + minSnooze + ":" + updateSecSnooze
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    while (snoozeAlarm != currentTime):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
        
    snoozeBut.grid()
    mixer.init()
    mixer.music.load("/home/pi/Documents/Python_Clock/Bill Conti - Gonna Fly Now (Theme From Rocky).mp3")
    mixer.music.play()
    
def setAlarm():
    #if hour, minute, or second is not in the form '00', concatenate 0 at the 0th position
    hour = str(hourBox.get()) 
    if (len(hour) < 2):
        hour = "0" + hour
        
    minute = str(minBox.get())
    if (len(minute) < 2):
        minute = "0" + minute
        
    second = str(secBox.get())
    if (len(second) < 2):
        second = "0" + second

    #compares current time to set alarm time and plays song
    alarmTime = hour + ":" + minute + ":" + second
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    while (alarmTime != currentTime):
        currentTime = time.strftime("%H:%M:%S", time.localtime())
    mixer.init()
    mixer.music.load("/home/pi/Documents/Python_Clock/Bill Conti - Gonna Fly Now (Theme From Rocky).mp3")
    mixer.music.play()
    snoozeBut.grid()
    
def stop():
    mixer.music.stop()
    snoozeBut.grid_remove()
    
#initialize widget buttons
setBut = Button(master, text="Set", bg="blue", activebackground="green" , command=setAlarm)
setBut.grid(column=2, row=1)

snoozeBut = Button(master, text="Snooze", bg="orange", activebackground="green", command=snooze)
snoozeBut.grid(column=4, row=1)
snoozeBut.grid_remove()

endBut = Button(master, text="Stop", bg="red", command=stop)
endBut.grid(column=3, row=1)


mainloop()
