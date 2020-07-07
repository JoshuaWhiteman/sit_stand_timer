import tkinter as tk
import time
from datetime import datetime

#Countdown
t = 0
def countdown():
    t = int(ent_timer.get())

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

frm_entry = tk.Frame(master=window)
ent_timer = tk.Entry(master=frm_entry, width=10)
lbl_sec = tk.Label(master=frm_entry, text="Seconds")

ent_timer.grid(row=0, column=0, sticky="e")
lbl_sec.grid(row=0, column=1, sticky="w")
frm_entry.grid(row=0, column=0, padx=10)

btn_start = tk.Button(master=window, text="START", command=countdown)
btn_start.grid(row=0, column=1, pady=10)

window.mainloop()