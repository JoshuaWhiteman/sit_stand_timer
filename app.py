import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, Text
import os

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

window = tk.Tk()
window.title("Sit Stand Timer")
# window.resizable(0,0)

# canvas = tk.Canvas(window, height=200, width=400, bg="#34bccf")
# canvas.pack()

frame = tk.Frame()
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# resetTimer = tk.Button(window, text="Reset", padx=10, pady=5, fg="white", bg="#34bccf")
# resetTimer.pack()

timer = tk.Label(text="frame 1 testing")
timer.pack()

window.mainloop()