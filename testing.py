import tkinter as tk
import time
from datetime import datetime

#Countdown
t = 0
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        display_countdown.set(timeformat)
        time.sleep(1)
        t -= 1
    print('SWITCH')

#tkinter UI design
window = tk.Tk()
window.title("Testing")

display_countdown = tk.StringVar()

frame_a = tk.Frame()
frame_a.pack()

label = tk.Label(master=frame_a, text="testing frame_a")
label.pack()

time_label= tk.Label(master=window, textvariable=display_countdown)
time_label.pack()

start_button = tk.Button(window, text="start", height=10, width=10, command=countdown(10))
start_button.pack()

window.mainloop()